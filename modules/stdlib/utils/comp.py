import os
import sys
import readline
import glob


class tabCompleter(object):
    """
    A tab completer that can either complete from
    the filesystem or from a list.

    Partially taken from:
    http://stackoverflow.com/questions/5637124/tab-completion-in-pythons-raw-input

    after that taken from a website i do not remember and extended
    """
    last_state = 0
    lst=None

    def __init__(self, com):
        self.coms = com

    def r(self, *argss, **kwargss):
        self.lst = None

    def pathCompleter(self, text, state):
        """
        This is the tab completer for systems paths.
        Only tested on *nix systems
        """
        line = readline.get_line_buffer().split()


        if self.lst ==  [None]:
            self.lst = None

        # replace ~ with the user's home dir. See https://docs.python.org/2/library/os.path.html
        if '~' in text:
            text = os.path.expanduser('~')

        if len(text.split()) < 2 and text.endswith(" "):
            text += "./"

        # autocomplete directories with having a trailing slash
        if os.path.isdir(text.split(" ")[-1]):
            text += '/'
        if state < self.last_state:
            self.lst = None
        if text.endswith("/"):
            text += "./"
        if self.lst==None and text == "":
            self.lst = []

            for i in self.coms:
                if i.startswith(text):
                    self.lst.append(i)
            self.lst.append(None)
        elif self.lst==None and "/" not in text:
            self.lst= []

            for i in self.coms:
                if i.startswith(text):
                    self.lst.append(i)


            for i in os.getenv("PATH").split(":"):
                if os.path.isdir(i):
                    i +="/"
                self.lst = self.lst + [x.replace("\\", "/").split("/")[-1]+" " for x in glob.glob(i+text + '*')]
            self.lst.append(None)
        elif self.lst==None:
            self.lst = [(" ".join(text.split(" ")[:-1])+" "+x) for x in glob.glob(text.split(" ")[-1] + '*')]
            self.lst.append(None)
            """if len(self.lst) > 1:
                tmp = self.lst[:]
                self.lst= []
                for i in tmp:
                    self.lst.append(i.split(" ")[-1])"""
        self.lst = self.lst[:-1]
        self.lst= [x.replace("/./", "/") for x in self.lst]
        self.lst = [x.replace("//", "/") for x in self.lst]
        self.lst.append(None)
        self.last_state = state
        return self.lst[state]


    def createListCompleter(self, ll):
        """
        This is a closure that creates a method that autocompletes from
        the given list.

        Since the autocomplete function can't be given a list to complete from
        a closure is used to create the listCompleter function with a list to complete
        from.
        """

        def listCompleter(text, state):
            line = readline.get_line_buffer()

            if not line:
                return [c + " " for c in ll][state]
                # print(1,[c + " " for c in ll][state],2)
            else:
                # print(3,[c + " " for c in ll if c.startswith(line)][state],4)
                return [c + " " for c in ll if c.startswith(line)][state]

        self.listCompleter = listCompleter