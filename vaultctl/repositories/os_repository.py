import ast
import os
import sys
from datetime import datetime
from getpass import getpass

import nacl.secret
import nacl.utils


def get_values():
    url = input('Entre com a URL (sem aspas): ')
    token = getpass('Entre com o token do usuário (sem aspas): ')
    secrets_dict = {'url': url, 'token': token}
    for i in range(1, 6):
        secrets_dict[f'key{i}'] = getpass(
            f'Entre com a chave {i} (sem aspas): '
        )
    return secrets_dict


def create_box():
    with open('../key_directory', 'r', encoding='utf-8') as kd_file:
        key_directory = kd_file.read()
        kd_file.close()
    try:
        with open(key_directory, 'rb') as key_file:
            key = key_file.read()
            key_file.close()
        return nacl.secret.SecretBox(key)
    except FileNotFoundError:
        print(
            'O arquivo de configuração key_directory não '
            'contém o endereço da chave de desencriptação.'
        )
        sys.exit()
    except IsADirectoryError:
        print(
            'O arquivo de configuração key_directory contém '
            'o endereço de um diretório. Forneça o endereço '
            'completo da chave.'
        )
        sys.exit()
    except PermissionError:
        print(
            'Erro de permissão. Verifique as permissões do arquivo e tente novamente.'
        )
        sys.exit()


def encode():
    secrets_dict = get_values()

    config_file_exists = os.path.exists(f'{os.getcwd()}/sct.hcv')

    if config_file_exists:
        print('*** ATENÇÃO!!! *** Já existe um arquivo de configuração.')
        today = datetime.today()
        today_str = today.strftime('%Y-%m-%d_%H-%M-%S')
        os.rename('sct.hcv', f'sct-backup-{today_str}.hcv')
        print(f'Arquivo renomeado para sct-backup-{today_str}.hvc')

    box = create_box()
    data = str(secrets_dict).encode('ascii')
    encrypted_data = box.encrypt(data)
    with open('sct.hcv', 'wb') as file:
        file.write(encrypted_data)
        file.close()


def decode():
    box = create_box()
    with open('sct.hcv', 'rb') as file:
        encrypted_data = file.read()
        file.close()
    data = box.decrypt(encrypted_data).decode()
    keys = ast.literal_eval(data)
    os.environ['URL'] = keys['url']
    os.environ['TOKEN'] = keys['token']
    for i in range(1, 6):
        os.environ[f'KEY{i}'] = keys[f'key{i}']
