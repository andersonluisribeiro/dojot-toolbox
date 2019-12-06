from . import Component, Optional, Scalable

class Persister(Component):

    def ask_use(self):
        self._vars['use_persister'] = Optional().ask_use("the persistence service")
        return self

    def ask_replicas(self):
        if self._vars['use_persister']:
            self._vars['persister_replicas'] = Scalable().ask_replicas(component="Persister", use=True)
        return self 