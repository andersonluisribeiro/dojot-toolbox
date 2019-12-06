from .component import Component
from .optional import Optional
from .scalable import Scalable
from .persistent import Persistent

import getpass

class Kong(Component):

    def __init__(self):
        super().__init__()
        self.__req_per_minute = 5
        self.__req_per_hour = 40
        self.__pg_username = "kong"
        self.__pg_password = "kong"
        self.__name = "API Gateway"         

    def ask_req_per_minute(self):
        try:
            self.__req_per_minute = int(input("\n\nHow many requests per minute are allowed? [{}] ".format( self.__req_per_minute )))
            return self
        except:
            return self

    def ask_req_per_hour(self):
        try:
            self.__req_per_hour = int(input("How many requests per hour are allowed? [{}] ".format( self.__req_per_hour )))
            return self
        except:
            return self        

    def ask_pg_username(self):
        username = input("Postgres username for {}? [{}] ".format( self.__name, self.__pg_username ))
        if username: self.__pg_username = username
        return self

    def ask_pg_password(self):
        password = getpass.getpass(prompt="Postgres password for {}? [{}] ".format( self.__name, self.__pg_password ), stream=None)
        if password: self.__pg_password = password
        return self   

    @property
    def vars(self):
        self._vars['apigw_req_per_minute'] = self.__req_per_minute
        self._vars['apigw_req_per_hour'] = self.__req_per_minute
        self._vars['apigw_pg_username'] = self.__pg_username
        self._vars['apigw_pg_password'] = self.__pg_password
        return self._vars