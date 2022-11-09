from modules.stdlib.utils.comp import tabCompleter
t = tabCompleter(["adc", "bdc", "acd"])



def getter(text):
    i = 0
    res = ""
    got = False
    while not got:
        a = t.pathCompleter(text, i)
        if type(a) != str:
            got = True
        else:
            res += a
            i+=1
    return res


print(getter("a"))
print(getter("b"))
