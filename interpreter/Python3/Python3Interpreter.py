import subprocess
from util.do_threaded import do_threaded


class Python3Interpreter:

    def __init__(self, code):
        self.process = subprocess.Popen("Action/Python3/venv/Scripts/python.exe",
                                        stdout=subprocess.PIPE,
                                        stdin=subprocess.PIPE)

        self.code = code

        self.process.stdin.write(code)

        do_threaded(self.image_listener)

        return

    def image_listener(self):

        def on_msg_receive(msg):
            # path = self.action_folder + "\\" + msg
            #             # self.set_image_path(path)
            print(msg)
            return

        while True:
            line = self.process.stdout.readline()
            if len(line) > 0:
                line = line.decode("utf-8")
                line = line.rstrip()
                on_msg_receive(line)

        return
