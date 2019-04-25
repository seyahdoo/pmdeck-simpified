
import zipfile

from interpreter.Python.PythonInterpreter import PythonInterpreter
from interpreter.AHK.AHKInterpreter import AHKInterpreter


class InterpreterLink:

    def __init__(self, file_path):
        zf = zipfile.ZipFile(file_path, 'r')
        items = zf.namelist()

        if "code.py" in items:
            print("its pythonic")
            self.interpreter = PythonInterpreter()

        elif "code.ahk" in items:
            print("its autohotkey")
            self.interpreter = AHKInterpreter()

        else:
            print("this button does not have code, returning.")
            return

        return



