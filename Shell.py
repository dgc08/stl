import os
from shutil import copy2
from importlib import import_module
from sys import executable, exit

try:
    import pwd
    os.getlogin = lambda: pwd.getpwuid(os.getuid())[0]
except ModuleNotFoundError:
    pass
rexist = False


try:
    import readline as r
    rexist = True
except ModuleNotFoundError:
    pass







def colored(s, col):
    cols = {"green":"\033[92m", "blue":"\033[94m"}
    return cols[col] + s + "\033[0m"

def system_wrapper(*args, **kwargs):
    return os.system(args[0])


class Shell():
    commanddict = {}
    used = []
    vars = {}
    script_path = ""
    forbidden = ["script_root", "__pycache__"]
    stl_no_double = False

    def cleanup(self):
        if self.stl_no_double:
            return
        os.remove(self.script_path+"/modules/tmp/__init__.py")
        copy2(self.script_path+"/modules/blank.py", self.script_path+"/modules/tmp/__init__.py")

    def __del__(self):
        self.cleanup()

    def shell(self):
        try:
            command = input("STL on '" + colored(os.getlogin(), "green") + "' || " + colored(os.getcwd(), "blue") + "> $ ")
        except KeyboardInterrupt:
            print("\n")
            return True
        except EOFError:
            print("\n")
            return False
        return self.compute(command)

    #do not modify this
    def emergency(self, com):
        if com == "STL_EM_EXIT":
            try:
                self.cleanup()
            except Exception as e:
                print("Cleanup failed:", str(e))
            exit(1)

    def compute(self, command, no_double = False):
        #do not modify
        self.emergency(command)



        command = command.strip()
        args = command.split(" ")

        # made it possible to use stl modules in something like pipes
        if isinstance(self.commanddict.get(args[0], command), str):
            is_STL_comm = self.commanddict.get(args[0], command).startswith("PY") or self.commanddict.get(args[0], command).startswith("2PY")
        else:
            is_STL_comm = False
        if not command.startswith("stl ") and command.strip() != "" and not command.startswith("PY") and not no_double and not is_STL_comm and not command.startswith("2PY"):
            command = executable + " " + self.script_path + " --no-double " + command
            os.system(command)
            return True

        bc = command
        # Command is set to is value in commanddict
        command = self.commanddict.get(args[0], command)
        # checks if the evaluated command is a command itself
        if command in self.commanddict:
            print("geez")
            return self.compute((command+" "+" ".join(args[1:])).strip())
        if callable(command):
            self._exec_func(command, *args)
        elif command.startswith("PY"):
            if command == "PY return":
                return False
            elif command == "PY rComp":
                if rexist:
                    self.t.r()
            elif command == "PY USE":
                if len(args) <2:
                    args.append(" ")
                if os.path.isfile(args[1]):
                    self.use(args[1])
                elif os.path.isfile(self.script_path+"/modules/extern/script_root/"+args[1]):
                    self.use(self.script_path+"/modules/extern/script_root/"+args[1])
                elif os.path.isfile(self.script_path+"/modules/extern/script_root/"+args[1]+".py"):
                    self.use(self.script_path+"/modules/extern/script_root/"+args[1]+".py")
                else:
                    print("File not found.")
            elif command == "PY USED":
                print("\n".join(self.used))
        else:
            args = [args[0], command]
            command = system_wrapper
            self._exec_func(command, *args)
        return True
    def load_extern(self):
        lst = os.listdir(self.script_path+"/modules/extern")
        lst += os.listdir(self.script_path+"/modules")
        for i in lst:
            if os.path.isdir(self.script_path+"/modules/extern/"+i)  and i not in self.forbidden:
                try:
                    tmp = import_module("modules.extern."+i)
                except Exception as e:
                    print("Could not activate module "+i+": "+str(e))
                    continue
                self.command_append(tmp)
                del(tmp)
        import modules.tmp as tmp

        self.command_append(tmp)

        del (tmp)


    def _exec_func(self, command, *args):
        try:
            command(*args[1:], stl_path=self.script_path, shell=self)
        except FileNotFoundError:
            print("No such file or dictionary.")
        except OSError as e:
            print(e)
        except KeyboardInterrupt:
            print("\n")
            return True
        except Exception as e:
            print("Module crashed: "+str(e))

    def use(self, file):
        copy2(file, self.script_path + "/modules/tmp/__init__.py")
        import modules.tmp as tmp

        self.command_append(tmp)

        del (tmp)


    def __init__(self):
        import modules.stdlib as stdlib
        self.command_append(stdlib)
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        self.load_extern()
        del (stdlib)

        if rexist:
            from modules.stdlib.utils.comp import tabCompleter
            r.set_completer()
            self.t = tabCompleter([i for i in self.commanddict.keys() if not i.startswith("2PY")])
            r.set_completer_delims('')
            r.parse_and_bind("tab: complete")

            r.set_completer(self.t.pathCompleter)

        self.compute(" ")

    def command_append(self, module):
        try:

            if hasattr(module, "vars"):
                self.vars = {**self.vars, **module.vars}

            self.commanddict = {**self.commanddict, **module.commanddict}
            if module.consts["type"] == "module" and module.consts["name"] not in self.used:
                self.used.append(module.consts["name"])
            for modu in module.modules:
                self.command_append(modu)
        except AttributeError:
            print("Module "+module.__name__+" seems not to be a stl module.")

