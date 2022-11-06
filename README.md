# VaultCtl

O Vault é uma ferramenta desenvolvida pela HashiCorp que armazena, protege e controla o acesso a tokens, senhas, certificados, chaves de criptografia, secrets e outros dados sensíveis.
Todas as informações ficam salvas em um cofre que podem ser acessadas por aplicações para autenticar no banco de dados, na AWS, etc.  

A ferramenta da HashiCorp tem um uso bastante simples, mas exige que o desenvolvedor fique consultando tokens e chaves para conectar e desbloquear o vault. 
Guardar essas informações em arquivos txt, bem como ficar copiando e colando-as no terminal pode ser enfadonho e inseguro.
Pensando nisso, desenvolvemos um script em python que guarda essas informações de forma criptografada, adicionando uma camada a mais de segurança, faz o bloqueio e desbloqueio do vault, exibe o token do usuário e as chaves (para o caso de acesso direto pelo terminal).  

Não desenvolvemos funções para adicionar ou consultar chaves dentro do vault, pois isso deve ser feito diretamente pela aplicação.

## Como usar

> vaultctl [option]  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; unseal, -u &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Desbloqueia o vault.  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; seal, -s &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bloqueia o vault.  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; status &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Exibe o status do vault.  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; token, -t &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Exibe o token do usuário.  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; keys, -k &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Exibe as chaves.   
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; help, -h &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Ajuda.

## Instalação*

> git clone git@github.com:fantunesdev/vaultcfg.git  
> cd vaultctl  
> chmod +x install.sh   
> sudo ./install.sh

*Script em desenvolvimento