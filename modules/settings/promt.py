import os

try:
    import pwd
    os.getlogin = lambda: pwd.getpwuid(os.getuid())[0]
except ModuleNotFoundError:
    pass

def colored(s, col):
    cols = {"green":"\033[92m", "blue":"\033[94m"}
    return cols[col] + s + "\033[0m"


def promt():
    return "STL on '" + colored(os.getlogin(), "green") + "' || " + colored(os.getcwd(), "blue") + "> $ "
