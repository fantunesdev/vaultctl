#!/bin/bash

PATH=$(pwd)
IFS='/'
read -a strarr <<< "$PATH"
SUBDIR_NUMBER=$((${#strarr[*]} - 1))
ACTUAL_DIR=${strarr[$SUBDIR_NUMBER]}
if [ $ACTUAL_DIR == 'vaultctl' ]; then
    echo "entrou"
    if [ $USER = 'root' ]; then
        cp vaultctl /usr/local/bin/

        if [ ! -d /var/lib/vaultctl ]; then
            mkdir /var/lib/vaultctl
        fi
        cp -rf * /var/lib/vaultctl/

        cd /var/lib/vaultctl/

        python3.10 -m venv venv
        source venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt

        vaultctl --configure
    else
        echo 'É necessário estar logado como root para realizar a instalação.'
    fi
else
    echo "Você está no diretório vaultctl. Por favor, acesse esse diretório para continuar a instalação."
fi
