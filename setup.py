from cx_Freeze import setup, Executable

base = None    

executables = [Executable("aimtrainer.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Merles Aimtrainer",
    options = options,
    version = "0.1",
    description = 'Weil du im Stream nach nem Aimtrainer gefragt hast!',
    executables = executables
)