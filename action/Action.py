import time

from window.Window import Window
from util.do_threaded import do_threaded

from interpreter.InterpreterLink import InterpreterLink


class Action:

    def __init__(self, file_path):

        # setup window
        self.window = Window(self)

        # setup interpreter
        self.interpreter_link = InterpreterLink(self, file_path)

        self.is_pressed = False

        self.on_initialize()

        self._updating = True
        self._update_thread = do_threaded(self._update_loop)

        return

    def set_image_base64(self, image_string):

        self._draw(image_string)
        return

    def _draw(self, image_string):
        self.window.set_image_base64(image_string)
        return

    def on_initialize(self):
        self.interpreter_link.interpreter.on_initialize()
        return

    def on_pressed(self):
        self.is_pressed = True
        self.interpreter_link.interpreter.on_pressed()
        return

    def on_released(self):
        self.is_pressed = False
        self.interpreter_link.interpreter.on_released()
        return

    def on_update(self):
        self.interpreter_link.interpreter.on_update()
        return

    def on_exit(self):
        self._updating = False
        self.interpreter_link.interpreter.on_exit()
        return

    def _update_loop(self):

        while self._updating:
            last_update = time.time()

            self.on_update()

            time_elapsed = time.time() - last_update
            if time_elapsed < 1:
                time.sleep(1-time_elapsed)
        return

