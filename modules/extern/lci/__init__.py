#! /usr/bin/python3

import os
import sys

options = []
compiler_settings = []

modules = []
consts = {"type":"module", "name":"lci", "description":"Shortcut for Compiling and running C/C++ Applications"}


def main(*args, **kwargs):
    options = ["gcc", "lci.out.put", False]
    for i in args:
        if i.startswith("---"):
            if i.startswith("---name="):
                options[1] = i.replace("---name=", "")
                options[2] = True
            elif i.startswith("---comm="):
                options[0] = i.replace("---comm=", "")
        else:
            compiler_settings.append(i)


#         Command               Compiler flags              Name of the file
    com = options[0] + " " + " ".join(compiler_settings) + " -o " + options[1]
    ret = os.system(com)

    print("\033[1;34;40mLCI:\033[1;37;40m Starting process...\033[0m")
    if ret == 0:
        os.system("chmod +rx " + options[1])
        com = "./" + options[1]
        os.system(com)
        if options[2]:
            pass
        else:
            os.remove(options[1])
    else:
        print("Compiler returned not 0")
    print()

commanddict = {"lci":main}

if __name__ == "__main__":
    main(*sys.argv[1:])
