
from . import simpletools
from . import builtins as builtinss

commanddict = {}
modules = [builtinss, simpletools]
consts = {"type":"parent", "name":"stdlib"}
vars = {}


del(simpletools)
