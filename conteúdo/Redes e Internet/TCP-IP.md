# Introdução a protocolos de rede -- TCP e IP

TCP/IP (Transmission Control Protocol/Internet Protocol) é um conjunto de protocolos usados para comunicação pela Internet e outras redes de computadores. É um bloco de construção fundamental das rede computacionais modernas e é usado por praticamente todos os computadores e dispositivos conectados à Internet. Nesta aula, vamos explorar os fundamentos da rede TCP/IP e seu uso no terminal Linux.

## Introdução aos protocolos

Os dois componentes de protocolo do TCP/IP lidam com diferentes aspectos da rede de computadores.

 - Protocolo de Internet – o **IP** de TCP/IP – é um protocolo sem conexão que lida apenas com o roteamento de pacotes de rede usando o *datagrama* IP como a unidade básica de informações de rede. O datagrama IP consiste em um cabeçalho seguido por uma mensagem.

 - O Protocolo de Controle de Transmissão – o **TCP** de TCP/IP – permite que hosts de rede estabeleçam conexões que podem ser usadas para trocar fluxos de dados. O TCP também garante que os dados enviados entre as conexões sejam entregues e que cheguem a um host de rede na mesma ordem em que foram enviados de outro host de rede.

No Linux, a stack do TCP/IP é incorporada ao kernel do sistema operacional, o que significa que todas as funções de rede são controladas pelo kernel. Isso permite uma experiência de rede mais eficiente e confiável, bem como maior segurança para as funções de rede.

Uma das ferramentas mais comuns usadas no terminal Linux para rede TCP/IP é o comando 'ping'. Este comando é usado para testar a conectividade entre dois dispositivos enviando pacotes ICMP (Internet Control Message Protocol) e recebendo respostas. Por exemplo, para testar a conectividade entre um computador Linux com endereço IP 192.168.1.10 e um roteador com endereço IP 192.168.1.1, podemos usar o seguinte comando:

```bash
$ ping 192.168.1.1
```

Esse comando envia pacotes ICMP para o roteador e aguardará uma resposta. Se o roteador responder, sabemos que há conectividade entre os dois dispositivos.

Outra ferramenta útil para rede TCP/IP no terminal Linux é o comando 'netstat'. Este comando exibe informações sobre conexões de rede ativas, tabelas de roteamento e outras estatísticas de rede. Por exemplo, para visualizar todas as conexões TCP ativas em um computador Linux, podemos usar o seguinte comando:

```bash
$ netstat -at
```

Este comando vai exibir uma lista de todas as conexões TCP, junto com seus endereços locais e remotos e o status atual da conexão.

## Conceitos básicos
### O Endereço IP

Todos os computadores em uma rede precisam ter um endereço. O esquema de endereçamento da Internet é baseado nos endereços IP. A versão original dos endereços IP, denominada de IPv4, consiste em um número de 32 bits separado em blocos de 8 bits. Estes endereços foram pensados para serem legíveis por humanos, mas com o crescimento da Internet, foi necessário a expansão da base de endereçamento para 128 bits, dando origem ao IPv6, que é bem menos legível.

### Classes de rede e máscaras
Originalmente os endereços eram divididos em blocos denominados [classes](https://en.wikipedia.org/wiki/Classful_network). Mas esta divisão a priori mostrou-se pouco eficiente, pois o espaço de endereços a ser buscados durante o [roteamento](https://en.wikipedia.org/wiki/Routing) era muito grande. Criou-se então o conceito de máscaras que definiam intervalos de endereços correspondentes a [sub-redes](https://en.wikipedia.org/wiki/Subnetwork). Desta forma todos os computadores em uma sub-rede têm o mesmo prefixo, por exemplo: 10.23.23.123 e 10.23.23.127 pertence a uma mesma sub-rede que pode ser identificada pela máscara 255.255.255.0.

#### Notação CIDR
[CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation) significa "Classless Inter-Domain Routing" é uma notação simplificada para representar máscaras de endereços.
Ela consiste de um endereço IP seguido de uma "/" e um número decimal. Este número decimal representa o número de bits "1" no início do endereço. Logo, 198.51.100.0/24 corresponte à seguinte máscara de subrede: 255.255.255.0 ou os endereços de 198.51.100.0 a 198.51.100.255

Para calcular quantos endereços estão disponíveis sob uma certa máscara basta usar a seguinte fórmula 2^(comp.do endereço-comp do prefixo). Existem [calculadoras online](https://mxtoolbox.com/subnetcalculator.aspx), que dão mais informações.

## Redes Privadas e NAT
Redes privadas não precisam ter endereços que sejam globalmente únicos. Então podem usar livremente todo o espaço de  endereçamento do IPv4 ou 6. Porém para comunicar-se com endereços da internet, precisam fazê-lo através de um protocolo denominado ["network address translation"](https://en.wikipedia.org/wiki/Network_address_translation)(NAT).

### NAT
![NAT](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/NAT_Concept-en.svg/1024px-NAT_Concept-en.svg.png)
A tradução de endereços entre a LAN (rede local) e a WAN (tipicamente a internet) se dá a nível de um [roteador](https://en.wikipedia.org/wiki/Router_(computing)).

Todos os pacotes IP possuem um endereço de origem e outro de destino. Quando estes pacotes passam por um NAT, vindo de uma rede privada, o seu endereço de origem é alterado, e quando chegam a uma rede privada o seu endereço de destino é alterado. Normalmente um host externo, em um cenário de NAT simétrico, não consegue enviar pacotes para um host na rede interna, a menos que seja uma resposta ao uma comunicação iniciada pelo host interno, pois cada transmissão iniciada internamente cria uma uma regra de tradução de endereçõs no NAT.

Quando 2 hosts em redes locais distintas querem se comunicar diretamente, estratégias de [travessia de NAT](https://en.wikipedia.org/wiki/TCP_hole_punching), precisam ser utilizadas, por exemplo para aplicações [P2P](https://en.wikipedia.org/wiki/Peer-to-peer).

## Protocolo TCP
O protocolo TCP diz respeito aos pacotes de dados a ser transmitidos entre dois computadores, Enquanto o pacote IP cuida do endereçamento, o TCP garante a integridade da comunicação anível dos bytes. O TCP prioriza a integridade dos dados sobre a velocidade de transmissão. Então aplicações que não requerem integridade absoluta, como o VOIP (telefonia IP) podem se utilizar de outros protocolos como o [UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol), por exemplo.
![TCP](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Tcp_state_diagram_fixed_new.svg/1920px-Tcp_state_diagram_fixed_new.svg.png)

Tanto o protocolo TCP quanto o UDP se utilizam de portas para identificar e trocar informaçẽs com aplicativos específicos em um host. As portas são identificadas por um número de 16 bits (0-65535) reservada pelo aplicativo envolvido na conexão TCPou UDP.

## Exercícios
Embora o Protocolo TCP tenha sido desenhado para comunicar-se através da internet, podemos utilizá-lo para comunicação entre programas rodando na mesma máquina.

Vamos explorar este conceito usando a Linguagem Python. Não se procupe se você ainda não conhece a linguagem, vamos explicar o funcionamento do código.

Vamos escrever dois programas um que vamos chamar de "servidor" e outro que será o "cliente".

```python
#!/usr/bin/env/python
# servidor_de_eco.py

import socket

HOST = "127.0.0.1"  # endereço IP da máquina local
PORT = 65432  # Porta em que vamos escutar (portas não privilegiadas > 1023).

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # cria o Socket
    s.bind((HOST, PORT)) # Conecta o socket ao host e porta
    s.listen() # começa a escutar...
    conn, addr = s.accept() # Aceita a conexão
    with conn:
        print(f"Connectado por {addr}")
        while True:
            data = conn.recv(1024) # Tenta receber dados
            if not data:
                break
            conn.sendall(data) # Envia de volta os dados (eco)
```

Agora o código do Cliente:

```python
#!/usr/bin/env python
# cliente_eco.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) 
    s.sendall(b"Oi, Tudo Bem?")
    data = s.recv(1024)

print(f"Received {data!r}")
```
### Executando o cliente e o servidor
Começamos nosso teste rodando primeiro o programa servidor
```bash
$ python servidor_de_eco.py
```
Depois iniciamos o cliente

```bash
$ python cliente_eco.py
```