from .component import Component
from .optional import Optional
from .scalable import Scalable
from .constants import gui as constants

class Gui(Component):

    def __init__(self):
        super().__init__()
        self.use = False
        self.replicas = 1
        self.name = "GUI"
        self.show_name(self.name)

    def get_use(self):
        return self.use

    def get_replicas(self):
        return self.replicas        

    def ask_use(self):
        self.use = Optional().ask_use(constants['use'].format(self.name))
        return self

    def ask_replicas(self):
        self.replicas = Scalable().ask_replicas(component=self.name, use=self.use)
        return self 

    @property
    def vars(self):
        self._vars['use_gui'] = self.use
        self._vars['gui_replicas'] = self.replicas
        return self._vars