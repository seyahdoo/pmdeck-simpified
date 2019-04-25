import time

import zipfile

from window.Window import Window
from util.do_threaded import do_threaded


class Action:

    def __init__(self, file_path):

        # setup window
        self.window = Window()

        # setup interpreter
        zf = zipfile.ZipFile(file_path, 'r')
        items = zf.namelist()
        if "code.py" in items:
            print("its pythonic")
        elif "code.ahk" in items:
            print("its autohotkey")
        else:
            print("this button does not have code, returning.")
            return

        self.is_visible = False
        self.is_pressed = False

        self.initialize()
        do_threaded(self._update_loop)
        return

    def _set_visible(self, space):
        self.is_visible = True
        self.current_space = space
        self.on_visible()
        self._draw()
        return

    def _set_invisible(self):
        self.is_visible = False
        self.on_invisible()
        return

    def set_image_base64(self, image_string):

        self._draw(image_string)
        return

    def _draw(self, image_string):
        if self.is_visible:
            self.window.set_image_base64(image_string)
        return

    def _pressed(self):
        self.is_pressed = True
        self.on_pressed()
        return

    def _released(self):
        self.is_pressed = False
        self.on_released()
        return

    def _update_loop(self):
        last_1_sec_update = time.time()

        while True:
            last_update = time.time()

            self.on_update()
            if last_update - last_1_sec_update > 1:
                self.on_update_sec()
                last_1_sec_update = last_update
            if self.is_pressed:
                self.on_hold_down()

            time_elapsed = time.time() - last_update
            if time_elapsed < 0.1:
                time.sleep(0.1-time_elapsed)
        return

    def initialize(self):
        return

    def on_visible(self):
        return

    def on_invisible(self):
        return

    def on_pressed(self):
        return

    def on_hold_down(self):
        return

    def on_released(self):
        return

    def on_update_sec(self):
        return

    def on_update(self):
        return

    def on_exit(self):
        return



