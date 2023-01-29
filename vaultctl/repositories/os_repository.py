import ast
import os
import socket
import sys
from datetime import datetime
from getpass import getpass

import nacl.exceptions
import nacl.secret
import nacl.utils


def get_values():
    url = input('Entre com a URL (sem aspas): ')
    url_is_valid = veryfy_url(url)
    if not url_is_valid:
        print(
            f'A url "{url}" não é válida. '
            f'Digite um ip/dns e uma porta separados por ":".\n'
            f'Exemplo: http://127.0.0.1:8200 ou http://localhost:8200.\n'
            f'OBS: 8200 é porta padrão do Vault. '
            f'Verifique as configurações do Vault.'
        )
        sys.exit(1)
    token = getpass('Entre com o token do usuário (sem aspas): ')
    secrets_dict = {'url': url, 'token': token}
    for i in range(1, 6):
        secrets_dict[f'key{i}'] = getpass(
            f'Entre com a chave {i} (sem aspas): '
        )
    return secrets_dict


def create_key():
    user_response = input('Você deseja criar uma chave criptográfica? (S/n): ')
    if user_response in ['n', 'N']:
        key_path = input('Entre com o endereço completo da chave: ')
        verify_existing_key(key_path)
    else:
        print('Criando chave criptográfica.')
        key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
        key_directory = input(
            'Entre com o endereço onde deseja salvar a chave: '
        )
        if key_directory[-1] != '/':
            key_directory += '/'
        key_path = f'{key_directory}pvt.key'
        with open('../key_directory.conf', 'w', encoding='utf-8') as kd_file:
            kd_file.write(key_path)
            kd_file.close()
        new_key = verify_new_key(key_directory, key)
        if not new_key:
            sys.exit(1)


def verify_existing_key(key_path: str):
    with open('../key_directory.conf', 'w+', encoding='utf-8') as kd_file:
        kd_file.write(key_path)
        kd_file.close()
    box = create_box()
    if box:
        print(f'Foi encontrada uma chave válida em {key_path}.')
    else:
        sys.exit(1)


def verify_new_key(key_directory: str, key: bytes):
    try:
        if not os.path.isdir(key_directory):
            raise NotADirectoryError
        with open(f'{key_directory}pvt.key', 'wb') as key_file:
            key_file.write(key)
            key_file.close()
        return True
    except NotADirectoryError:
        print(f'O diretório {key_directory} não existe.')
        return None
    except PermissionError:
        print(
            'Erro de permissão. Verifique as permissões do arquivo e tente novamente.'
        )
        return None


def veryfy_url(url: str):
    try:
        protocol, nothing, path = url.split('/')
        ip, port = path.split(':')
        port = int(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if not port == 8200:
            print(
                f'ATENÇÃO! Você selecionou a porta {port}. '
                f'A porta padrão do Vault é 8200. '
                f'Ignore este aviso se a porta configurada '
                f'for realmente diferente. '
                f'Caso contrário, cancele (Ctrl + C) e tente novamente.'
            )
        if result == 0:
            return True
        return False
    except ValueError:
        return False
    except socket.gaierror:
        return False


def create_box():
    with open('../key_directory.conf', 'r', encoding='utf-8') as kd_file:
        key_path = kd_file.read()
        kd_file.close()
    try:
        with open(key_path, 'rb') as key_file:
            key = key_file.read()
            key_file.close()
        return nacl.secret.SecretBox(key)
    except FileNotFoundError:
        print(f'Arquivo não encontrado. Você digitou: {key_path}')
        return None
    except IsADirectoryError:
        if not key_path[-1] == '/':
            key_path += '/'
        print(
            f'"{key_path}" é um diretório. '
            f'Digite o caminho completo da chave e tente novamente.\n'
            f'Exemplo: {key_path}pvt.key'
        )
        return None
    except PermissionError:
        print(
            'Erro de permissão. Verifique as permissões do arquivo e tente novamente.'
        )
        return None
    except nacl.exceptions.ValueError:
        print(f'O arquivo {key_path} não contém uma chave válida.')
        return None


def configure_vaultctl():
    create_key()
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
