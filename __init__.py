# Support for using stl as module
from . import Shell

stl_Shell = Shell
Shell = stl_Shell.Shell

del(stl_Shell)
