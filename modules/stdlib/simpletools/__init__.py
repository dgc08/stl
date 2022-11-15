from . import cnstall
from . import simplealias

commanddict = {"cnstall":cnstall.main}
modules = []
consts = {"type":"module", "name":"simpletools"}
vars = {}

commanddict = {**commanddict, **simplealias.comm}

del(cnstall)