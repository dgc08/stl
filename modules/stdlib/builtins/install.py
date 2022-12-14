from shutil import copy2
from importlib import import_module
from os import mkdir
from shutil import rmtree

def install_stl(module, type="-a", *args, **kwargs):
    #TODO
    sh = kwargs["shell"]
    if type=="-a":
        m = module.replace(".py", "").replace(".stl", "")
        dirr = kwargs["stl_path"]+"/modules/extern/"+m
        try:
            mkdir(kwargs["stl_path"]+"/modules/extern/"+m)
        except FileExistsError:
            pass
        copy2(module, dirr+"/"+"__init__.py")

        #TODO call install function
    if type=="--help":
        pass
    if type=="-s":
        copy2(module, kwargs["stl_path"]+"/modules/extern/script_root/")
    if type=="-r":
        print(kwargs["stl_path"]+"/modules/extern/"+module)
        rmtree(kwargs["stl_path"]+"/modules/extern/"+module)
    try:
        sh.load_extern()
    except Exception as e:
        rmtree(kwargs["stl_path"] + "/modules/extern/" + m)
        print("Failed (un)installing module: " + str(e))
        return
