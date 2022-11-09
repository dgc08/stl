from modules.stdlib.builtins.cd import cd
from modules.stdlib.builtins.install import install_stl

commanddict = {"exit":"PY return", "cd":cd, "use":"PY USE", "used":"PY USED", "stp":install_stl}
modules = []
consts = {"type":"module", "name":"builtins"}
vars = {}
