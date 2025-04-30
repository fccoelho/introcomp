# Começando um projeto em Python do Zero
Neste documento vamos aprender como começar um projeto Python. Usando dois package managers, o `uv`, e o `poetry`.

## A ferramenta Poetry
O [Poetry](https://python-poetry.org/) é uma ferramenta que facilita muito a criação e gerenciamento de um projeto. Nós vamos usa-la neste exercício. Para instalar o Poetry siga os passos [nesta página](https://python-poetry.org/docs/)

## Inicializando o Projeto
Vamos começar  criando um diretório para o projeto, vamos chamá-lo de autoreport, pois nosso projeto consistirá na construção de um gerador de relatórios analíticos em LaTeX. O código final do 

```bash
$ mkdir autoreport
$ cd autoreport
$ poetry init
```
Após instalar o poetry no Windows é necessário adicionar o Poetry ao PATH para isso use o seguinte comando do terminal `cmd`

```
set PATH=%PATH%;%USERPROFILE%\AppData\Roaming\pypoetry\venv\Scripts
```

O comando `poetry init` vai criar um arquivo `pyproject.toml` que contém as informações do projeto. Você pode editar este arquivo para adicionar informações sobre o projeto, como o nome, versão, licença, etc.

## Adicionando dependências
As dependências de um projeto podem ser de dois tipos: **dependências de desenvolvimento**, que são necessárias para desenvolver o projeto, mas não são necessárias para executá-lo, e **dependências de execução**, que são necessárias para executar o projeto. Por exemplo, o projeto que estamos criando depende do pacote `jinja2` para gerar os relatórios, mas não depende do pacote `pytest` para executar o projeto. Por outro lado, o pacote `pytest` é necessário para executar os testes do projeto, mas não é necessário para executar o projeto em si.

Vamos começar adicionando o pacote `jinja2` como dependência de execução do projeto. Para isso, execute o seguinte comando:

```bash
$ poetry add jinja2
```

O poetry vai adicionar o pacote `jinja2` como dependência de execução do projeto e vai atualizar o arquivo `pyproject.toml` com esta informação. 

agora vamos adicionar o pacote `pytest` como dependência de desenvolvimento:

```bash
$ poetry add --dev pytest
```
Note que  identificamos as dependências de desenvolvimento com a opção `--dev`. O poetry vai adicionar o pacote `pytest` como dependência de desenvolvimento do projeto e vai atualizar o arquivo `pyproject.toml` com esta informação.

## Instalando as dependências
Para instalar as dependências do projeto, execute o seguinte comando:

```bash
$ poetry install
```
Este comando vai criar um ambiente virtual para o projeto e instalar as dependências nele. O ambiente virtual é um diretório que contém uma instalação do Python e as dependências do projeto. O poetry cria o ambiente virtual dentro do diretório `.venv` na raiz do projeto.

## Criando a estrutura básica do projeto
Vamos começar a estruturar o projeto criando um diretório chamado `relatório` que será o pacote principal do projeto. Dentro deste diretório, vamos criar um arquivo `__init__.py` vazio. Este arquivo indica ao Python que o diretório `relatório` é um pacote Python. Vamos criar outro diretório, chamado `tests` na raiz do nosso projeto para conter os testes do nosso código:

```bash
$ mkdir relatorio
$ touch relatorio/__init__.py
$ mkdir tests
```

Dentro do diretório `relatorio` vamos adicionar um diretório chamado `templates` para conter os templates dos relatórios. Vamos criar um arquivo chamado `cria.py` dentro do diretório `relatorio` para conter o código do nosso pacote.

O conteúdo destes diretórios será desenvolvido em sala de aula e você pode acompanhar o desenvolvimento do projeto [neste repositório](https://github.com/fccoelho/autoreport).
