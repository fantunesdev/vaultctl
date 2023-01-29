import os
import sys

import system_messages
from repositories import os_repository, vault_repository

try:
    param = sys.argv[1]

    if param in ['unseal', '-u']:
        vault_repository.unseal_vault()
        print('Vault is unseal.')
    elif param in ['seal', '-s']:
        vault_repository.seal_vault()
        print('Vault is seal.')
    elif param in ['token', '-t']:
        token = vault_repository.get_user_token()
        print(token)
    elif param in ['url', '-U']:
        url = vault_repository.get_url()
        print(url)
    elif param in ['keys', '-k']:
        try:
            keys = vault_repository.get_keys()
            for i in range(1, 6):
                print(os.getenv(f'KEY{i}'))
        except UserWarning:
            print('Root privilegies are needed.')
    elif param == 'status':
        vault_repository.get_status()
    elif param in ['help', '-h']:
        system_messages.print_options()
    elif param == '--configure':
        os_repository.configure_vaultctl()
    else:
        raise IndexError
except IndexError:
    system_messages.print_options()
