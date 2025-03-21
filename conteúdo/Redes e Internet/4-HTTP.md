# O Protocolo HTTP
O Protocolo de Transferência de Hipertexto (HTTP) é um protocolo de comunicação utilizado para transferir informações na World Wide Web. O HTTP é a base da comunicação de dados na web, e é utilizado para transferir páginas web, imagens, vídeos, arquivos, entre outros. O HTTP é um protocolo de camada de aplicação, e é baseado no modelo cliente-servidor, onde um cliente faz uma requisição a um servidor, que responde com uma resposta.

## História do HTTP
O HTTP foi desenvolvido por Tim Berners-Lee no CERN em 1989, e foi padronizado pela IETF (Internet Engineering Task Force) em 1996. O HTTP é um protocolo simples e extensível, e é baseado no modelo de requisição-resposta, onde um cliente faz uma requisição a um servidor, que responde com uma resposta. O HTTP é um protocolo sem estado, o que significa que cada requisição é independente das outras, e o servidor não mantém informações sobre requisições anteriores.
## Características do HTTP
O HTTP é um protocolo de comunicação baseado em texto, e utiliza uma sintaxe simples para definir as mensagens de requisição e resposta. As mensagens HTTP são compostas por uma linha de status, um cabeçalho e um corpo. A linha de status define o status da requisição ou resposta, o cabeçalho define os metadados da mensagem, como o tipo de conteúdo, a codificação, a data, entre outros, e o corpo define o conteúdo da mensagem, como o HTML de uma página web, a imagem de um arquivo, o vídeo de um vídeo, entre outros.

## Métodos HTTP
O HTTP define vários métodos para interagir com recursos na web. Os métodos mais comuns são:
1. `GET`: Obtém um recurso do servidor.
2. `POST`: Envia dados para o servidor.
3. `PUT`: Atualiza um recurso no servidor.
4. `DELETE`: Deleta um recurso no servidor.
5. `HEAD`: Obtém os cabeçalhos de um recurso.
6. `OPTIONS`: Obtém os métodos suportados por um recurso.
7. `PATCH`: Atualiza parcialmente um recurso no servidor.
8. `TRACE`: Realiza um teste de loopback no servidor.
9. `CONNECT`: Conecta-se a um servidor por meio de um proxy.

### Versões do HTTP
O HTTP possui várias versões, sendo as mais comuns o HTTP/1.1 e o HTTP/2. O HTTP/1.1 é a versão mais utilizada atualmente, e é baseada em conexões TCP, onde cada requisição é feita em uma conexão separada. O HTTP/2 é uma versão mais recente do HTTP, e é baseada em conexões multiplexadas, onde várias requisições podem ser feitas em uma única conexão.

O HTTP/3 é a versão mais recente do HTTP, publicada em 2022, e é baseada no protocolo QUIC, que é um protocolo de transporte baseado em UDP. O HTTP/3 é mais rápido e seguro que o HTTP/2, e é recomendado para aplicações web modernas.


## Sessão HTTP
O HTTP é um protocolo sem estado, o que significa que cada requisição é independente das outras, e o servidor não mantém informações sobre requisições anteriores. Para manter o estado entre requisições, o HTTP utiliza cookies e sessões. Os cookies são pequenos arquivos de texto armazenados no navegador do cliente, e são utilizados para armazenar informações sobre o usuário, como preferências, autenticação, entre outros. As sessões são uma forma de manter o estado entre requisições, e são armazenadas no servidor. As sessões são identificadas por um ID de sessão, que é enviado para o cliente por meio de um cookie.

### Cookies
Os cookies são pequenos arquivos de texto armazenados no navegador do cliente, e são utilizados para armazenar informações sobre o usuário, como preferências, autenticação, entre outros. Os cookies são enviados pelo servidor para o cliente por meio do cabeçalho `Set-Cookie`, e são enviados pelo cliente para o servidor por meio do cabeçalho `Cookie`. Os cookies são armazenados no navegador do cliente e são enviados para o servidor em cada requisição subsequente.

## Códigos de Status HTTP
O HTTP define uma série de códigos de status para indicar o resultado de uma requisição. Os códigos de status são divididos em cinco classes:
1. `1xx`: Informacional - A requisição foi recebida e está sendo processada.
2. `2xx`: Sucesso - A requisição foi bem-sucedida.
3. `3xx`: Redirecionamento - A requisição foi redirecionada.
4. `4xx`: Erro do cliente - A requisição contém erros.
5. `5xx`: Erro do servidor - O servidor encontrou um erro ao processar a requisição.

A tabela abaixo lista os códigos de status mais comuns:

| Código | Descrição            | Significado                                                                 |
|--------|----------------------|-----------------------------------------------------------------------------|
| 200    | OK                   | A requisição foi bem-sucedida.                                              |
| 301    | Movido Permanentemente | O recurso foi movido permanentemente para outra URL.                       |
| 400    | Requisição Inválida  | A requisição contém erros de sintaxe.                                      |
| 401    | Não Autorizado       | O cliente não está autorizado a acessar o recurso.                        |
| 403    | Proibido             | O cliente não tem permissão para acessar o recurso.                        |
| 404    | Não Encontrado       | O recurso não foi encontrado.                                               |
| 500    | Erro Interno do Servidor | O servidor encontrou um erro ao processar a requisição.                   |
| 503    | Serviço Indisponível | O servidor não está disponível no momento.                                 |


## Segurança no HTTP
O HTTP é um protocolo de comunicação inseguro, pois as mensagens são transmitidas em texto puro, o que torna fácil para um atacante interceptar e modificar as mensagens. Para garantir a segurança das comunicações, o HTTP utiliza o protocolo HTTPS (HTTP Secure), que é uma versão segura do HTTP baseada em criptografia SSL/TLS. O HTTPS utiliza certificados digitais para autenticar os servidores e criptografar as mensagens, garantindo a confidencialidade, integridade e autenticidade das comunicações.

## Interação com o HTTP usando Python
O Python possui várias bibliotecas para interagir com o HTTP, como o `requests`, que é uma biblioteca simples e fácil de usar para fazer requisições HTTP. Abaixo está um exemplo de como fazer uma requisição GET usando o `requests`:

```python
import requests
response = requests.get('https://www.example.com')
print(response.text)
```

Na biblioteca padrão do Python, temos o módulo `http.server`, que permite criar um servidor HTTP simples. Abaixo está um exemplo de como criar um servidor HTTP simples usando o `http.server`:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>Hello, World!</h1></body></html>')
server = HTTPServer(('localhost', 8000), MyHandler)
server.serve_forever()
``` 
Nesse exemplo, criamos uma classe `MyHandler` que herda da classe `BaseHTTPRequestHandler`. A classe `MyHandler` define o método `do_GET`, que é chamado quando uma requisição GET é feita para o servidor. O método `do_GET` envia uma resposta HTTP 200 OK, define o cabeçalho `Content-type` como `text/html`, e escreve o conteúdo da página HTML no arquivo `wfile`.

Para acessar o servidor, basta rodar o seguinte código cliente:

```python
import requests
response = requests.get('http://localhost:8000')
print(response.text)
```