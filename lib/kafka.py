from .component import Component
from .optional import Optional
from .scalable import Scalable
from .persistent import Persistent

class Kafka(Component):

    def __init__(self):
        super().__init__()
        self.__replicas = 1
        self.__persistence_time = 168
        self.__volume_use = False
        self.__volume_size = 10
        self.name = "Apache Kafka"

    @property
    def persistence_time(self):
        return self.__persistence_time            

    def ask_persistence_time(self):
        try:
            self.__persistence_time = int(input("\n\nHow many hours would you like the data to be kept in Apache Kafka (0 for indeterminate)? [168] "))
            return self
        except:
            return self

    def ask_persistence_volume(self):
        self.__volume_use = Persistent().ask_persistence_volume(component=self.name)
        return self

    def ask_volume_size(self):
        self.__volume_size = Persistent().ask_volume_size(component=self.name, use=self.__volume_use, default=self.__volume_size)
        return self


    @property
    def vars(self):
        self._vars['kafka_replicas'] = self.__replicas
        self._vars['kafka_persistence_time'] = self.__persistence_time
        self._vars['kafka_persistence_volume'] = self.__volume_use
        self._vars['kafka_volume_size'] = self.__volume_size
        return self._vars