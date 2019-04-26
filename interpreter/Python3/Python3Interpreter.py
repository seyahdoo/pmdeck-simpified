import subprocess
from util.do_threaded import do_threaded

import tempfile
import os
import sys

import atexit


class Python3Interpreter:

    def __init__(self, action, code):

        self.action = action

        glue_file = open("interpreter/Python3/Glue.py")
        glue_code = glue_file.read()

        self.code_file_descriptor, self.code_file_path = tempfile.mkstemp()
        os.write(self.code_file_descriptor, code)
        os.write(self.code_file_descriptor, glue_code.encode())
        os.close(self.code_file_descriptor)

        # code_file = open(self.code_file_path, 'w')
        # code_file.write(code.decode())
        # code_file.write(glue_code)
        # code_file.close()

        print(self.code_file_path)

        self.process = subprocess.Popen("interpreter/Python3/venv/Scripts/python.exe {}"
                                        .format(self.code_file_path),
                                        stdout=subprocess.PIPE,
                                        stdin=subprocess.PIPE)

        atexit.register(self.atexit)

        do_threaded(self.image_listener)

        return

    def image_listener(self):

        def on_msg_receive(msg: str):
            # path = self.action_folder + "\\" + msg
            #             # self.set_image_path(path)

            if msg[0:9] == "SETIMAGE:":
                base64image = msg[9:]
                self.action.set_image_base64(base64image)

            return

        while True:
            line = self.process.stdout.readline()
            if len(line) > 0:
                line = line.decode("utf-8")
                line = line.rstrip()
                on_msg_receive(line)

        return

    def on_initialize(self):
        self.process.stdin.write("on_initialize\n".encode("utf-8"))
        self.process.stdin.flush()
        return

    def on_pressed(self):
        self.process.stdin.write("on_pressed\n".encode("utf-8"))
        self.process.stdin.flush()
        return

    def on_released(self):
        self.process.stdin.write("on_released\n".encode("utf-8"))
        self.process.stdin.flush()
        return

    def on_update(self):
        self.process.stdin.write("on_update\n".encode("utf-8"))
        self.process.stdin.flush()
        return

    def on_exit(self):
        self.process.stdin.write("on_exit\n".encode("utf-8"))
        self.process.stdin.flush()
        self.process.terminate()
        os.remove(self.code_file_path)
        return

    def atexit(self):
        print("exiting")
        self.on_exit()
        return
