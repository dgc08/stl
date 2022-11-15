from os import name, path

commanddict = {}
modules = []
consts = {"type":"module", "name":"repl_snt"}



def replacer(rpt):
        if rpt.startswith("~"):
                cpathl = list(rpt)
                cpathl[0] = path.expanduser("~")
                rpt = "".join(cpathl)

        return rpt

vars = {"cdreplacer": replacer}
