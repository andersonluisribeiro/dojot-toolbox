from .component import Component
from .optional import Optional
from .scalable import Scalable
from .persistent import Persistent
from .authenticable import Authenticable
from .quantifiable import Quantifiable
from .constants import devm as constants

import getpass

class DeviceManager(Component):

    def __init__(self):
        super().__init__()
        self.__pg_username = "devm"
        self.__pg_password = "devm"
        self.__name = constants['name']
        self.__authenticable = Authenticable()         
        self.__quantifiable = Quantifiable()

    def ask_pg_username(self):
        self.__pg_username = self.__authenticable.ask_username(constants['pg_user'].format( self.__name, self.__pg_username ), self.__pg_username)
        return self

    def ask_pg_password(self):
        self.__pg_password = self.__authenticable.ask_password(constants['pg_password'].format( self.__name, self.__pg_password ), self.__pg_password)
        return self   

    @property
    def vars(self):
        self._vars['devm_pg_username'] = self.__pg_username
        self._vars['devm_pg_password'] = self.__pg_password
        return self._vars