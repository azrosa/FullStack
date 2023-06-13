import sys
from cx_Freeze import setup, Executable


build_exe_options = {'packages': ['PyQt6', 'mysql', 'xml', 'hashlib'],
                     'include_files': ['controller', 'data', 'img', 'model', 'view']}

base = None
if sys.platform == "win32":
    base == "Win32GUI"

setup(
    name="Sistema Bancário",
    version="1.0",
    description="Sistema bancário",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)
