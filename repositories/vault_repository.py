import os

import hvac
import dotenv

from repositories import os_repository

dotenv.load_dotenv()


def unseal_vault():
    os_repository.decode()
    client = hvac.Client(url=os.environ['URL'])
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
    client = hvac.Client(url=os.environ['URL'])
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
