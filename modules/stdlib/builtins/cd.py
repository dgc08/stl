from os import chdir, getcwd


def cd(*args, **kwargs):
    try:
        cpath = args[0]
    except IndexError:
        print((getcwd()))
        return

    if "cdreplacer" in kwargs["shell"].vars:
        if callable(kwargs["shell"].vars["cdreplacer"]):
            cpath = kwargs["shell"].vars["cdreplacer"](cpath)

    chdir(cpath)
