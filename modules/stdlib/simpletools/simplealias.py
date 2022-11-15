from os import name

comm = {}

if name == "nt":
    comm["ls"] = "dir"
