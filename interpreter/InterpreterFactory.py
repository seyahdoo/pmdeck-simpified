

# TODO still not decided to be using this pattern

import zipfile

from interpreter.Python3.Python3Interpreter import Python3Interpreter
from interpreter.AHK.AHKInterpreter import AHKInterpreter


def create_interpreter(file_path):
    zf = zipfile.ZipFile(file_path, 'r')
    items = zf.namelist()

    if "code.py" in items:
        print("its pythonic")
        code_file = zf.open("code.py")
        code = code_file.read()
        return Python3Interpreter(code)

    elif "code.ahk" in items:
        print("its autohotkey")
        return AHKInterpreter()

    else:
        print("this button does not have code, returning.")
        return

    return

