from Shell import Shell
from sys import argv

continue_sh = True
sh = Shell()

if len(argv)<2:
    while continue_sh:
        continue_sh = sh.shell()
else:
    command=" ".join(argv[1:])
    sh.compute(command)

