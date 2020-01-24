from .component import Component
from .optional import Optional
from .persistent import Persistent
from .optional import Optional
from .disk import Disk
from .quantifiable import Quantifiable
from .authenticable import Authenticable
from .constants import persistence as constants


class Persistence(Component):

    def __init__(self):
        super().__init__()
        self._visible_name = constants['name']
        self.__use_persistent_volume = False
        self.__postgres_volume_size = 10
        self.__mongo_volume_size = 10
        self.__persistent = Persistent()
        self.__optional = Optional()
        self.__quantifiable = Quantifiable()
        self.__disk = Disk()

    def ask_for_all_services(self, question=constants['persistence_use']):
        try:
            self.ask_if_use_persistent_volume(question) \
                .and_postgres_volume_size() \
                .and_mongo_volume_size()    
        except ValueError as e:
                print("\n{}".format(e))
                self.__disk = Disk()
                self.ask_for_all_services(constants['persistence_confirmation'])

    def ask_if_use_persistent_volume(self, question=constants['persistence_use']):
        self.__use_persistent_volume = self.__optional.ask_use(
            question)
        return self

    def and_postgres_volume_size(self):
        if self.__use_persistent_volume:
            question = constants['postgres'].format(self.__disk.free_space(), self.__postgres_volume_size)
            volume_size = self.__quantifiable.ask_quantity(question)
            self.__disk.alocate(volume_size)
            self.__postgres_volume_size = volume_size
            
        return self

    def and_mongo_volume_size(self):
        if self.__use_persistent_volume:
            question = constants['mongodb'].format(self.__disk.free_space(), self.__mongo_volume_size)
            volume_size = self.__quantifiable.ask_quantity(question)
            self.__disk.alocate(volume_size)
            self.__mongo_volume_size = volume_size
            
        return self    

    @property
    def vars(self):
        self._vars['dojot_psql_persistent_volumes'] = self.__use_persistent_volume
        self._vars['dojot_psql_local_persistent_volumes'] = self.__use_persistent_volume
        # self._vars['dojot_psql_volume_size'] = self.__volume_size
        return self._vars
