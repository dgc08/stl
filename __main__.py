from Shell import Shell
from sys import argv

no_double = False

continue_sh = True
sh = Shell()
if "--no-double" in argv:
    argv.remove("--no-double")
    no_double = True

if len(argv)<2:
    while continue_sh:
        continue_sh = sh.shell()
else:
    command=" ".join(argv[1:])
    sh.compute(command, no_double)

