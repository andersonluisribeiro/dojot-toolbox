from termcolor import colored

class Component:
    def __init__(self):
        self._vars = {}

    def show_name(self, name):
        print(colored("\n\n{}".format(name), 'green'))
        return self
