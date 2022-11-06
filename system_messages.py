

def print_menu():
    print('#' * 49)
    print('#' * 3, ' ' * 12, 'HASHICORP VAULT', ' ' * 12, '#' * 3)
    print('#' * 49)
    print()
    print('1 - Desselar Vault.')
    print('2 - Selar Vault.')
    print('3 - Imprimir token')
    print('4 - Imprimir chaves')
    print('5 - Criar .env.')
    print('6 - Limpar o conteúdo do arquivo .env.')
    print('0 - Sair')
    print()


def print_success_message(message):
    print(f'\033[1:32m{message}\033[m')


def print_error_message(message):
    print(f'\033[1:32m{message}\033[m')


def print_options():
    print('''
usage: vaultctl [option]
  unseal, -u        Unseal your vault.
  seal, -s          Seal your vault.
  token, -t         Get user token.
  keys, -k          Get keys.
  status            Get vault status.
            ''')
