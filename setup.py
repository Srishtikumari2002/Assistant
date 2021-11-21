import cx_Freeze
import sys
import matplotlib

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("ARJUN.py", base=base, icon="logo.ico")]

cx_Freeze.setup(
    name = "Arjun",
    options = {"build_exe":{"packages": ["tkinter", "pyttsx3", "wolframalpha", "requests", "PIL", "speech_recognition", "webbrowser", "wikipedia"], "include_files":["logo.ico", "arjun.png", "google.png", "credentials.json", "mic.png", "send.png", "user.png", "token.pickle", "smalltalkdownloader.py"]}},
    version = "0.0.2",
    author='Shubham Tiwari',
    author_email='shubhamtiwaripython2004@gmail.com',
    description = "A personal desktop assistant",
    executables = executables

    )
