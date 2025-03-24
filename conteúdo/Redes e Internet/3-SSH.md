# SSH - Secure Shell
O SSH ou Secure Shell é um protocolo de rede que permite a troca de dados de forma segura entre dois dispositivos. O SSH é muito utilizado para acessar servidores remotos, pois permite a execução de comandos de forma segura, e também para transferir arquivos de forma segura entre dois dispositivos.

## História
O SSH foi desenvolvido por Tatu Ylönen em 1995, com o objetivo de substituir o protocolo Telnet, que era utilizado para acessar servidores remotos, mas que não era seguro, pois os dados eram transmitidos de forma não encriptada. O SSH foi desenvolvido para ser uma alternativa segura ao Telnet, e desde então, se tornou um dos protocolos mais utilizados para acessar servidores remotos.

## Conceitos Básicos
### Chave Pública e Chave Privada
O SSH utiliza um par de chaves para autenticar o cliente e o servidor. O par de chaves é composto por uma chave pública e uma chave privada. A chave pública é compartilhada com o servidor, e a chave privada é mantida em segredo pelo cliente. Quando o cliente se conecta ao servidor, o servidor envia um desafio criptográfico para o cliente, que é assinado com a chave privada do cliente, e o servidor verifica a assinatura com a chave pública do cliente. Se a assinatura for válida, o servidor autentica o cliente.

Para criar um par de chaves SSH, basta digitar o comando `ssh-keygen` seguido do nome do arquivo de chave. Por exemplo, para criar um par de chaves chamado `id_rsa` e `id_rsa.pub`, basta digitar o comando abaixo.

```bash
ssh-keygen -t rsa -b 4096 -C "
```


### Conexão segura
O SSH utiliza criptografia para garantir uma conexão segura entre o cliente e o servidor. Isso protege contra ataques de interceptação, como ataques de homem no meio, garantindo que os dados transmitidos não possam ser lidos por terceiros.

### Conexão SSH
Para se conectar a um servidor remoto via SSH, basta digitar o comando `ssh` seguido do nome de usuário e do endereço do servidor. 

```bash
ssh localhost
```

O comando acima irá se conectar ao servidor `localhost` com o usuário atual. Se o usuário for diferente, basta digitar o nome de usuário seguido do `@` e do endereço do servidor.

```bash
ssh usuario@localhost
```

### Transferência de arquivos com SSH
O SSH também pode ser utilizado para transferir arquivos de forma segura entre dois dispositivos. Para transferir um arquivo de um dispositivo para outro, basta digitar o comando `scp` seguido do nome do arquivo e do endereço do servidor. Por exemplo, para transferir o arquivo `arquivo.txt` para o servidor `ssh.example.com`, basta digitar o comando `scp` seguido do nome do arquivo e do endereço do servidor.

```bash
scp arquivo.txt usuario@localhost:/diretorio/destino
```
Para copiar um arquivo do servidor para o cliente, basta inverter a ordem dos argumentos.

```bash
scp usuario@localhost:/diretorio/origem/arquivo.txt .
```

### Execução de comandos remotos
O SSH também pode ser utilizado para executar comandos de forma remota em um servidor. Para executar um comando remoto, basta digitar o comando `ssh` seguido do nome de usuário e do endereço do servidor, seguido do comando que você deseja executar.

```bash
ssh usuario@localhost ls
```


### Túneis SSH
O SSH também pode ser utilizado para criar túneis seguros entre dois dispositivos. Isso permite que portas de um servidor sejam mapeadas para portas locais, permitindo o acesso a serviços remotos de forma segura. Para criar um túnel SSH, basta digitar o comando `ssh` seguido do argumento `-L` e das portas que você deseja mapear. Por exemplo, para mapear a porta 8000 do servidor para a porta 80 do cliente, basta digitar o comando abaixo.

```bash
ssh -L 80:localhost:8000 -f -NC usuario@servidor.remoto
```
a opção `-f` faz com que o ssh seja executado em segundo plano, e a opção `-N` faz com que nenhum comando seja executado no servidor remoto. A opção `-C` ativa a compressão dos dados, o que pode melhorar o desempenho em conexões lentas.

O tunelamento também pode ser feito de forma reversa, mapeando portas locais para portas remotas. Para isso, basta utilizar o argumento `-R` no comando `ssh`. Por exemplo, para mapear a porta 80 do cliente para a porta 8000 do servidor, basta digitar o comando abaixo.

```bash
ssh -R 8000:localhost:80 -f -NC usuario@servidor.remoto
```

