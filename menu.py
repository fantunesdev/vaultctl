import system_messages
from repositories import vault_repository, os_repository

while True:
    system_messages.print_menu()

    try:
        user_response = int(input('Escolha uma das opções: '))

        if user_response == 1:
            vault_repository.unseal_vault()
        elif user_response == 2:
            vault_repository.seal_vault()
        elif user_response == 3:
            token = vault_repository.get_user_token()
            system_messages.print_success_message(f'\nToken: {token}\n')
        elif user_response == 4:
            keys = vault_repository.get_keys()
            system_messages.print_success_message('\nChaves:\n')
            for key in keys:
                system_messages.print_success_message(key)
            print()
        elif user_response == 5:
            os_repository.create_dotenv_file()
            system_messages.print_success_message('Arquivo .env criado com sucesso!')
        elif user_response == 6:
            os_repository.clean_dotenv_file()
            system_messages.print_success_message('O conteúdo do arquivo .env foi apagado com sucesso!')
        elif user_response == 627:
            os_repository.encode()
        elif user_response == 0:
            break
        else:
            raise ValueError

    except ValueError:
        system_messages.print_error_message('Você não digitou uma opção válida.')
