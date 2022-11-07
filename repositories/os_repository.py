import base64
import ast
import os
from datetime import datetime

from getpass import getpass


def get_values():
    url = input('Entre com a URL (sem aspas): ')
    token = getpass('Entre com o token do usuário (sem aspas): ')
    secrets_dict = {
        'url': url,
        'token': token
    }
    for i in range(1, 6):
        secrets_dict[f'key{i}'] = getpass(f'Entre com a chave {i} (sem aspas): ')
    return secrets_dict


def encode():
    secrets_dict = get_values()
    content = str(secrets_dict)
    config_file_exists = os.path.exists(f'{os.getcwd()}/.sct.hcv')

    if config_file_exists:
        print('*** ATENÇÃO!!! *** Já existe um arquivo de configuração.')
        today = datetime.today()
        today_str = today.strftime('%Y-%m-%d_%H-%M-%S')
        os.rename('.sct.hcv', f'.sct-backup-{today_str}.hcv')
        print(f'Arquivo renomeado para .sct-backup-{today_str}.hvc')

    with open('.sct.hcv', 'w', encoding='utf-8') as file:
        content_bytes = content.encode('ascii')
        base64_content = base64.b64encode(content_bytes)
        content_str = str(base64_content)
        file.write(content_str)
        file.close()


def decode():
    with open('.sct.hcv', 'r', encoding='utf-8') as file:
        content = file.read()
        code = content.split("\'")[1]
        string = str(base64.b64decode(code)).split('\"')[1]
        keys = ast.literal_eval(string)
        file.close()
    os.environ['URL'] = keys['url']
    os.environ['TOKEN'] = keys['token']
    for i in range(1, 6):
        os.environ[f'KEY{i}'] = keys[f'key{i}']


def create_dotenv_file():
    decode()
    with open('.env', 'w', encoding='utf-8') as file:
        file.write(f'URL = {os.getenv("URL")}\n')
        file.write(f'TOKEN = {os.getenv("TOKEN")}\n')
        for i in range(1, 6):
            file.write(f'KEY{i} = {os.getenv(f"KEY{i}")}\n')
        file.close()


def clean_dotenv_file():
    os.remove('.env')
    with open('.env', 'w', encoding='utf-8') as file:
        file.close()
