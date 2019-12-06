from .component import Component
from .optional import Optional
from .scalable import Scalable

class Cron(Component):

    def __init__(self):
        super().__init__()
        self.use = False
        self.replicas = 1
        self.name = "Cron"

    def get_use(self):
        return self.use

    def get_replicas(self):
        return self.replicas        

    def ask_use(self):
        self.use = Optional().ask_use(component=self.name)
        return self

    def ask_replicas(self):
        self.replicas = Scalable().ask_replicas(component=self.name, use=self.use)
        return self 

    @property
    def vars(self):
        self._vars['use_cron'] = self.use
        self._vars['cron_replicas'] = self.replicas
        return self._vars