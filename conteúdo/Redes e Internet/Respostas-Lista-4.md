Abaixo você pode encontrar respostas resumidas para os exercícios da Lista 4 de Redes e Internet.

1. Um protocolo de comunicação é um conjunto de regras que governam a troca de dados em uma rede.
2. Os principais protocolos de comunicação utilizados na Internet incluem HTTP, HTTPS, FTP, SMTP, IMAP, POP3, TCP/IP, UDP, entre outros.
3. Um endereço IP é um identificador único para um dispositivo em uma rede.
IPv4 pode representar 2^32 endereços distintos, enquanto IPv6 pode representar 2^128 endereços distintos.
4. Um endereço MAC é um identificador único atribuído a uma interface de rede para comunicações na camada física de uma rede.
1. Um servidor DNS é um servidor que traduz nomes de domínio em endereços IP.
1. Uma rede local (LAN) é uma rede que conecta computadores e outros dispositivos em uma área geográfica limitada, como uma casa, escola, prédio de escritórios, etc.
1. A faixa de endereços IP reservada para redes em uma rede cujo IP basico é 192.168.0.0 cuja máscara é 255.255.255.0 é 192.168.0.0 - 192.168.0.255.
1. A notação CIDR é uma forma de especificar quais endereços IP estão incluídos em uma rede. A faixa de endereços IP reservada para redes em uma rede cuja máscara CIDR é /24 é 192.168.0.0 - 192.168.0.255.
1. O protocolo HTTP transmite informações na forma de páginas da web (HTML, CSS, JavaScript, imagens, etc.).
1. HTTPS significa HTTP Secure. É uma versão segura do protocolo HTTP que usa criptografia para proteger a comunicação.
1. O comando scp pode ser usado para copiar um arquivo de um computador para outro via SSH.
1. O comando ping pode ser usado para verificar se um computador está acessível via rede.
1. SSH usa chaves públicas para autenticação, permitindo que você se conecte a um servidor sem precisar digitar uma senha.
1. A porta padrão usada pelo protocolo SSH é a 22.
2. Para criar um túnel SSH, você deve usar o seguinte comando:
```bash
ssh -N -f -D 8080 [user@]server.com
```
Essa configuração abre uma conexão SSH em segundo plano (-N) e ativa um proxy dinâmico na porta local 8080 (-D). A opção -f permite que a sessão seja iniciada em segundo plano, enquanto o proxy se conectará ao
servidor remoto.
16. Para acessar um servidor FTP de forma anônima, geralmente você usa o usuário 'anonymous'.
1. O comando ls pode ser usado para listar os arquivos de um servidor FTP.
1. O comando get pode ser usado para copiar um arquivo de um servidor FTP para o seu computador.
1. Para copiar vários arquivos binários de um servidor FTP, cuja terminação seja .zip, você pode usar o comando mget.