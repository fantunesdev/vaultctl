import os
import sys

import system_messages
from repositories import vault_repository, os_repository

try:
    param = sys.argv[1]

    if param == 'unseal' or param == '-u':
        vault_repository.unseal_vault()
        print('Vault is unseal.')
    elif param == 'seal' or param == '-s':
        vault_repository.seal_vault()
        print('Vault is seal.')
    elif param == 'token' or param == '-t':
        token = vault_repository.get_user_token()
        print(token)
    elif param == 'keys' or param == '-k':
        keys = vault_repository.get_keys()
        for i in range(1, 6):
            print(os.getenv(f'KEY{i}'))
    elif param == 'status':
        vault_repository.get_status()
    elif param == 'help' or param == '-h':
        system_messages.print_options()
    elif param == '--first-config':
        os_repository.encode()
    else:
        raise IndexError
except IndexError:
    system_messages.print_options()
