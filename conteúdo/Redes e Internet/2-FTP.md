# Protocolo FTP
O Protocolo FTP ou File transfer Protocol,  é um protocolo desenvolvido para transferir arquivos entre um servidor e um cliente. Neste protocolo o cliente se autentica através de um usuário e uma senha, mas diverso servidores FTP també aceitam conexões anônimas.

Por questões de segurança A maioria dos servidores modernos se utilizam de uma conexão SSH para encriptação dos dados sendo denominados SFTP.

## Uso básico do FTP
Para começar a aprender como utilizar o FTP vamos começar utilizando o cliente de FTP que já vem instalado no Linux, o `ftp`. Para acessar um servidor FTP basta digitar o comando `ftp` seguido do endereço do servidor. Por exemplo, para acessar o servidor ftp.dca.fee.unicamp.br, basta digitar o comando `ftp geoftp.ibge.gov.br`. Após isso, o cliente irá pedir o nome de usuário e senha, e após a autenticação, o cliente irá mostrar o prompt `ftp>`, onde você pode digitar os comandos do cliente.

```bash
ftp geoftp.ibge.gov.br
``` 

No servidor do IBGE nos autenticaremos como usuário `anonymous` sem senha, e após a autenticação, podemos listar os arquivos do servidor com o comando `ls`, e para baixar um arquivo, basta digitar o comando `get` seguido do nome do arquivo. Por exemplo, para baixar os mapas do Brasil, precisamos navegar até o diretório `cartas_e_mapas/bases_cartograficas_continuas/bc250/versao2023/geopackage/`, e baixar o arquivo chamado `bc250_2023_11_23.zip`.

```bash
ftp> ls
ftp> cd cartas_e_mapas/bases_cartograficas_continuas/bc250/versao2023/geopackage/
ftp> get bc250_2023_11_23.zip
```

## Comandos do cliente FTP
O cliente FTP possui diversos comandos que podem ser utilizados para navegar e transferir arquivos entre o cliente e o servidor. Abaixo estão listados alguns dos comandos mais utilizados:
1. `ls`: Lista os arquivos do diretório atual.
2. `cd`: Navega para o diretório especificado.
3. `get`: Baixa um arquivo do servidor.
4. `put`: Envia um arquivo para o servidor.
5. `mget`: Baixa múltiplos arquivos do servidor.
6. `mput`: Envia múltiplos arquivos para o servidor.
7. `quit`: Encerra a conexão com o servidor.
8. `help`: Mostra a lista de comandos do cliente.
9. `pwd`: Mostra o diretório atual do servidor.
10. `mkdir`: Cria um diretório no servidor.
11. `rmdir`: Remove um diretório no servidor.
12. `delete`: Remove um arquivo no servidor.
13. `rename`: Renomeia um arquivo no servidor.
14. `binary`: Muda o modo de transferência para binário.
15. `ascii`: Muda o modo de transferência para ASCII.
16. `prompt`: Ativa ou desativa a confirmação de transferência de arquivos.
17. `hash`: Ativa ou desativa a exibição de um hash de progresso durante a transferência de arquivos.
18. `status`: Mostra o status da conexão com o servidor.

## Criando um servidor FTP
Em sua máquina local, você pode criar um servidor FTP para compartilhar arquivos com outros dispositivos. Para isso, você pode instalar um servidor FTP como o `vsftpd` e configurá-lo para compartilhar arquivos. Para instalar o `vsftpd`, basta digitar o comando abaixo.

```bash
sudo apt install vsftpd
```

Após a instalação, você pode configurar o servidor editando o arquivo de configuração `/etc/vsftpd.conf`. Você pode configurar o servidor para permitir conexões anônimas, definir o diretório raiz do servidor, definir as permissões de leitura e escrita, entre outras configurações. Modifique as seguintes configurações:
```bash
anonymous_enable=YES
local_enable=YES
write_enable=YES
anon_root=/var/ftp
```
Pode ser necessário criar o diretório raiz do servidor e definir as permissões corretas. Para isso, basta digitar os comandos abaixo.

```bash
sudo mkdir /var/ftp
sudo chown nobody:nogroup /var/ftp
sudo chmod a-w /var/ftp
```


Após configurar o servidor, você pode reiniciá-lo com o comando abaixo.

```bash
sudo service vsftpd restart
```

Para acessar o servidor, basta digitar o endereço do servidor no navegador ou em um cliente FTP, e autenticar-se com o usuário `anonymous` e senha "". Você pode transferir arquivos para o servidor utilizando um cliente FTP como o `ftp` ou o `FileZilla`.

## Exercicios
    1. Utilize o cliente FTP para acessar o servidor ftp.datasus.gov.br e baixar o arquivo `dissemin/publicos/Dados_Abertos/SINAN/DIC_DADOS_CHIKUNGUNYA_fev2024.pdf` para o seu computador.
    2. Usando apenas ferramentas do terminal do Linux, extraia o texto do PDF e descubra quais campos da tabela de Chikungunya estão associadas com a "Dengue".

## Referências
- [FTP - Wikipedia](https://en.wikipedia.org/wiki/File_Transfer_Protocol)


