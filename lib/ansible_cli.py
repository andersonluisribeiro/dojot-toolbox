import json
import shutil
import os
from progress.bar import Bar
from ansible.module_utils.common.collections import ImmutableDict
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.vault import VaultLib
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.playbook import Playbook
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
from ansible.module_utils._text import to_bytes
from ansible.parsing.vault import VaultSecret
from ansible import context

import ansible.constants as C


class ResultCallback(CallbackBase):
   
    def v2_runner_on_ok(self, result, **kwargs):
        host = result._host
        # print(json.dumps({host.name: result._result}, indent=4))


class AnsibleCLI:

    def encrypt_vars_file(self):
        vault = "ansible-vault encrypt --vault-id ./ansible-dojot/credential ansible-dojot/vars.yaml"
        os.system(vault) == 0 
    
    def run_playbook(self):
        context.CLIARGS = ImmutableDict(connection='local', module_path=None, forks=10, become=None,
                                become_method=None, become_user=None, check=False, diff=False, extra_vars={'@ansible-dojot/vars.yaml'})

        loader = DataLoader()
        loader.set_vault_secrets([('default', VaultSecret(_bytes=to_bytes('123')))])
        passwords = dict(vault_pass='123')

        results_callback = ResultCallback()

        inventory = InventoryManager(loader=loader, sources=('ansible-dojot/inventories/example_local',))

        variable_manager = VariableManager(loader=loader, inventory=inventory)

        playbook = Playbook.load('ansible-dojot/deploy.yaml', variable_manager=variable_manager, loader=loader)

        with Bar('Deploying dojot ', max=9) as bar:
            tqm = None
            try:
                for play in playbook.get_plays():
                    tqm = TaskQueueManager(
                            inventory=inventory,
                            variable_manager=variable_manager,
                            loader=loader,
                            passwords=passwords,
                            stdout_callback=results_callback,
                        )
                    tqm.run(play)
                    bar.next()
            finally:
                bar.finish
                if tqm is not None:
                    tqm.cleanup()                        
