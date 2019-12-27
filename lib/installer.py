import json
import os
import time
import yaml
import sys
import getpass
from termcolor import colored
from pyfiglet import Figlet
from . import Gui, Cron, Repository
from .ansible_cli import AnsibleCLI
from .constants import installer as constants

class Installer():
    def __init__(self, argv):
        self.vars = {}
        self.argv = argv
        self.ansible_cli = AnsibleCLI()

    def is_for_configuration(self):
        return len(self.argv) > 1 and self.argv[1] == "configure"  

    def should_deploy(self):
        return len(self.argv) > 2 and self.argv[2] == "--deploy"           

    def clone_repository(self):
        Repository().clone()          

    def say_wellcome(self):
        f = Figlet(font='speed')
        print(colored(f.renderText('dojot'), 'white'))
        print(colored("Welcome to Dojot CLI", 'white', attrs=['bold']))

    def say_thanks(self):
        print("\n\nThanks!\n")

    def say_bye(self):
        print("\n\nBye!\n")         

    def create_credentials_file(self):
        with open(r'ansible-dojot/credential', 'w') as file:
           file.write(getpass.getpass(prompt="\nSet you password for encrypt vars file: ", stream=None))       

    def create_vars_file_from(self, components):
        if not isinstance(components, list):
            raise ValueError("A list of components is necessary for create vars file")

        for component in components:
            self.vars.update(component.vars)

        with open(r'ansible-dojot/vars.yaml', 'w') as file:
            if any(self.vars):
                yaml.dump(self.vars, file)  
                
        return self        

    def encrypt_vars_file(self):
        self.ansible_cli.encrypt_vars_file()
    
    def call_ansible(self):
        self.create_credentials_file()
        self.encrypt_vars_file()
        if self.should_deploy():
            print('\n')
            self.ansible_cli.run_playbook()
        

        

        