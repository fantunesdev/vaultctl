import base64
import ast
import os


def encode():
    teste_list = {
        'url': os.getenv('URL'),
        'token': os.getenv('TOKEN'),
        'key1': os.getenv('KEY1'),
        'key2': os.getenv('KEY2'),
        'key3': os.getenv('KEY3'),
        'key4': os.getenv('KEY4'),
        'key5': os.getenv('KEY5')
    }

    content = str(teste_list)

    with open('sct.hcv', 'w', encoding='utf-8') as file:
        content_bytes = content.encode('ascii')
        base64_content = base64.b64encode(content_bytes)
        content_str = str(base64_content)
        file.write(content_str)
        file.close()


def decode():
    with open('sct.hcv', 'r', encoding='utf-8') as file:
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
