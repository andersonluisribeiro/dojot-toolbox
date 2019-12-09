import os
import sys
from git import Repo, Git

class Repository:

    def __init__(self):
        self.repo_dir = 'ansible-dojot'

    def repo_already_exists(self):
        return os.path.isdir('./{}'.format(self.repo_dir))

    def ask_use_existent_repo(self):
        res = input("\nYou already have a ansible-dojot repository. Do you want to use that? (y/n) [n] ")
        return True if res == "y" else False

    def exit(self):
        print("\nSo delete or change the installer directory before use it!")
        print("\nThanks!\n")  
        sys.exit(0)

    def make_clone(self):
        Git(".").clone("https://github.com/dojot/ansible-dojot.git")
        cloned_repo = Repo(self.repo_dir)
        cloned_repo.git.checkout('release/v0.4.1')     

    def clone(self):
        if self.repo_already_exists():
            use_existent_repo = self.ask_use_existent_repo()
            if use_existent_repo:
                return
            else:
                self.exit()

        self.make_clone()    
