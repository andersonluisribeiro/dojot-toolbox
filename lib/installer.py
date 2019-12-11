import json
import os
import time
import yaml
import sys
import getpass
from termcolor import colored
from pyfiglet import Figlet
from . import Gui, Cron, Repository

class Installer():
    def __init__(self, argv):
        self.vars = {}
        self.argv = argv

    def is_for_configuration(self):
        return len(self.argv) > 1 and self.argv[1] == "configure"    

    def using(self, component):
        component.vars = self.vars
        return component    

    def clone_repository(self):
        Repository().clone()          

    def say_wellcome(self):
        f = Figlet(font='speed')
        print(colored(f.renderText('dojot'), 'red'))
        print(colored("Welcome to Dojot CLI", 'green', attrs=['bold']))

    def say_thanks(self):
        print("\n\nThanks!\n")     

    def create_credentials_file(self):
        with open(r'ansible-dojot/credential', 'w') as file:
           file.write(getpass.getpass(prompt="\nSet you password for encrypt vars file: ", stream=None))       

    def create_vars_file_for(self, components):
        if not isinstance(components, list):
            raise ValueError("A list of components is necessary for create vars file")

        for component in components:
            self.vars.update(component.vars)

        with open(r'ansible-dojot/vars.yaml', 'w') as file:
            if any(self.vars):
                yaml.dump(self.vars, file)  
                
        return self        

    def encrypt_vars_file(self):
        vault = "ansible-vault encrypt --vault-id ./ansible-dojot/credential ansible-dojot/vars.yaml"
        os.system(vault) == 0 
    
    def call_playbook(self):
        playbook = "ansible-playbook -u cpqd -K -k -i inventories/example_local deploy.yaml -e @vars.yaml --vault-id ./credential"
        if os.system(playbook) == 0:
            os.remove("credential")

    def call_ansible(self):
        self.create_credentials_file()
        self.encrypt_vars_file()
        

        

        