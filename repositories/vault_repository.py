import os

import hvac

from repositories import os_repository


def unseal_vault():
    os_repository.decode()
    client = hvac.Client(url=os.getenv('URL'))
    if client.sys.is_sealed():
        client.token = os.getenv('TOKEN')
        key1 = os.getenv('KEY1')
        key2 = os.getenv('KEY2')
        key3 = os.getenv('KEY3')
        client.sys.submit_unseal_key(key1)
        client.sys.submit_unseal_key(key2)
        client.sys.submit_unseal_key(key3)
    return client


def seal_vault():
    client = hvac.Client(url=os.getenv('URL'))
    client.sys.seal()


def get_user_token():
    os_repository.decode()
    return os.getenv('TOKEN')


def get_keys():
    keys_list = []
    os_repository.decode()
    for i in range(1, 6):
        keys_list.append(os.getenv(f'KEY{i}'))
    return keys_list


def get_status():
    try:
        client = hvac.Client(url=os.getenv('URL'))
        response = client.seal_status

        print(f'''Seal Type       {response['type']}
Initialized     {response['initialized']}
Sealed          {response['sealed']}
Total Shares    {response['n']}
Threshold       {response['t']}
Version         {response['version']}
Build Date      {response['build_date']}
Storage Type    {response['storage_type']}
Cluster Name    {response['cluster_name']}
Cluster ID      {response['cluster_id']}
HA Enabeld      {client.ha_status['ha_enabled']}
        ''')
    except hvac.exceptions.VaultDown:
        print('Vault is seal. Please unseal vault.')
    except KeyError:
        print('Vault is seal. Please unseal vault.')
