# Começando um projeto em Python do Zero
Neste documento vamos aprender como começar um projeto Python.

## A ferramenta Poetry
O [Poetry](https://python-poetry.org/) é uma ferramenta que facilita muito a criação e gerenciamento de um projeto. Nós vamos usa-la neste exercício. Para instalar o Poetry siga os passos [nesta página](https://python-poetry.org/docs/)

## Inicializando o Projeto
Vamos começar  criando um diretório para o projeto, vamos chamá-lo de autoreport, pois nosso projeto consistirá na construção de um gerador de relatórios analíticos em LaTeX.

```bash
$ mkdir autoreport
$ cd autoreport
$ poetry init
```
Após instalar o poetry no Windows é necessário adicionar o Poetry ao PATH para isso use o seguinte comando do terminal `cmd`

```
set PATH=%PATH%;%USERPROFILE%\AppData\Roaming\pypoetry\venv\Scripts
```
