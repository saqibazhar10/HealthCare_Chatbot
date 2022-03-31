from cx_Freeze import setup, Executable

base = None    

executables = [Executable("win1.py", base=base)]

packages = ["idna","sys","numpy","PyQt5","pandas","sklearn","win32com.client"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "HealthCare",
    options = options,
    version = "1",
    description = 'Chatbot',
    executables = executables
)