
import zipfile

from interpreter.Python3.Python3Interpreter import Python3Interpreter
from interpreter.AHK.AHKInterpreter import AHKInterpreter


class InterpreterLink:

    def __init__(self, action, file_path):
        zf = zipfile.ZipFile(file_path, 'r')
        items = zf.namelist()

        if "code.py" in items:
            code_file = zf.open("code.py")
            code = code_file.read()
            self.interpreter = Python3Interpreter(action, code)

        elif "code.ahk" in items:
            print("its autohotkey")
            self.interpreter = AHKInterpreter()

        else:
            print("this button does not have code, returning.")
            return

        return



