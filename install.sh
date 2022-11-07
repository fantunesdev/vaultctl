#!/bin/bash

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
