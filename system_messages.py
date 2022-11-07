

def print_success_message(message):
    print(f'\033[1:32m{message}\033[m')


def print_error_message(message):
    print(f'\033[1:31m{message}\033[m')


def print_options():
    print('''usage: vaultctl [option]
  -u, unseal        Unseal your vault.
  -s, seal          Seal your vault.
  status            Get vault status.
  -t, token         Get user token.
  -k, keys          Get keys.
  -h, help          Get help.
  --configure       Set vault values.
            ''')
