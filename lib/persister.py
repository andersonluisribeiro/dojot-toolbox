from . import Component, Optional

class Persister(Component):

    def ask_use(self):
        self.variables['use_persister'] = Optional().ask_use("the persistence service")
        return self

    def ask_replicas(self):
        if self.variables['use_persister']:
            self.variables['persister_replicas'] = Scalable().ask_replicas()
        return self 