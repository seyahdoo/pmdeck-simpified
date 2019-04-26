import base64
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QMenu
from PyQt5.QtWidgets import QLabel

from util.do_threaded import do_threaded


class Window:

    def __init__(self,action):

        self.action = action
        self.always_on_top = False
        self.frame_enabled = False

        do_threaded(self.window_thread)

        return

    def window_thread(self):
        self.app = QApplication(sys.argv)
        self.ex = App(self)
        self.ex.mousePressEvent = self.pressed
        self.ex.mouseReleaseEvent = self.released

        self.app.exec_()

        print("Window Closed")
        return

    def set_image_base64(self, base64image):

        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(base64.b64decode(base64image))
        pixmap = pixmap.scaled(64, 64)
        self.ex.label.setPixmap(pixmap)

        return

    def pressed(self, event):
        modifiers = self.app.keyboardModifiers()

        if event.button() == QtCore.Qt.LeftButton and modifiers != Qt.AltModifier:
            print("Left click pressed")
            self.action.on_pressed()
        elif event.button() == QtCore.Qt.LeftButton and modifiers == Qt.AltModifier:
            print("dragging")

        return

    def released(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            print("Left click released")
            self.action.on_released()

        return

    def closed(self):

        return


class App(QWidget):

    def __init__(self, window):
        super().__init__()

        self.window = window

        self.title = 'PMDECK'
        self.left = 10
        self.top = 10
        self.width = 64
        self.height = 64

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

        self.label = QLabel(self)
        base64image = "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"

        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(base64.b64decode(base64image))
        pixmap = pixmap.scaled(64, 64)
        self.label.setPixmap(pixmap)

        self.show()

    def contextMenuEvent(self, event):
        menu = QMenu(self)

        setAlwaysOnTopAction = menu.addAction("Always On Top")
        setPreserveOnBootAction = menu.addAction("Preserve On Boot")
        setFrameEnabledAction = menu.addAction("Frame Enabled")
        quitAction = menu.addAction("Quit")

        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAction:
            self.window.app.quit()
        elif action == setAlwaysOnTopAction:
            self.window.always_on_top = not self.window.always_on_top

            if self.window.always_on_top:
                self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
            else:
                self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

            self.show()

        elif action == setPreserveOnBootAction:
            pass
        elif action == setFrameEnabledAction:

            self.window.frame_enabled = not self.window.frame_enabled

            if self.window.frame_enabled:
                self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.FramelessWindowHint)
            else:
                self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

            self.show()

