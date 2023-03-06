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