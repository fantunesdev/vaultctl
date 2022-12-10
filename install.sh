#!/bin/bash

ACTUAL_PATH=$(pwd)
IFS='/'
read -a STR_LIST <<< "$ACTUAL_PATH"
SUBDIR_NUMBER=$((${#STR_LIST[*]} - 1))
ACTUAL_DIR=${STR_LIST[$SUBDIR_NUMBER]}
if [ $ACTUAL_DIR == 'vaultctl' ]; then
    if [ $USER = 'root' ]; then
        cp vaultctl.sh /usr/bin/vaultctl

        if [ ! -d /var/lib/vaultctl ]; then
            mkdir /var/lib/vaultctl
        fi
        cd ..
        cp -rf vaultctl /var/lib/vaultctl/

        cd /var/lib/vaultctl/

        python3.10 -m venv venv
        source venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt

        if [ -f /var/lib/vaultctl/.sct.hcv ]; then
            echo "Já existe um arquivo com as chaves configurado. Será possível fazer essa configuração mais tarde com o comando vaultctl --configure"
            echo "Deseja sobrescrevê-lo? (s/N)"
            read USER_RESPONSE
            if [ $USER_RESPONSE == 's' -o $USER_RESPONSE == 'S' ]; then
                vaultctl --configure
            fi
        else
            vaultctl --configure
        fi
    else
        echo 'É necessário estar logado como root para realizar a instalação.'
    fi
else
    echo "Você não está no diretório vaultctl. Por favor, acesse esse diretório e tente novamente."
fi
