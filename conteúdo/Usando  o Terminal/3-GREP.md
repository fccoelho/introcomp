# O aplicativo GREP
O [GREP](https://en.wikipedia.org/wiki/Grep) é um aplicativo que permite a busca de padrões em arquivos de texto. Ele é muito útil para encontrar informações em arquivos de texto, como por exemplo, encontrar o nome de um usuário em um arquivo de log. Ele se utiliza de expressões regulares para realizar a busca.

## Expressões regulares
Uma [expressão regular](https://en.wikipedia.org/wiki/Regular_expression) é uma sequência de caracteres que especifica um padrão de busca. Ela é composta por caracteres literais e metacaracteres. Os caracteres literais são os caracteres que você deseja encontrar na busca. Já os metacaracteres são caracteres especiais que indicam ações especiais na busca.

### Caracteres literais
Os caracteres literais são os caracteres que você deseja encontrar na busca. Por exemplo, se você deseja encontrar a palavra "teste" em um arquivo, você pode utilizar a expressão regular `teste` para realizar a busca.

### Metacaracteres
Os [metacaracteres](https://en.wikipedia.org/wiki/Metacharacter) são caracteres especiais que indicam ações especiais na busca. Por exemplo, se você deseja encontrar a palavra "teste" em um arquivo, você pode utilizar a expressão regular `teste` para realizar a busca. Porém, se você deseja encontrar a palavra "teste" seguida de um espaço em branco, você pode utilizar a expressão regular `teste\s` para realizar a busca.

exemplo:
```bash
$ echo "teste teste" | grep "teste\s"
teste teste
```

### Usando o GREP para encontrar padrões em arquivos
O GREP pode ser utilizado para encontrar padrões em arquivos de texto. Por exemplo, se você deseja encontrar a palavra "teste" em um arquivo chamado `arquivo.txt`, você pode utilizar o comando abaixo:
```bash
$ grep "teste" 3-GREP.md
```
Um exemplo mais avançado é buscar por linhas que não contém a palavra "teste" em um arquivo chamado `3-GREP.md`:
```bash
$ grep -v "teste" 3-GREP.md
```

### Usando o GREP para encontrar padrões em arquivos e exibir o número da linha
O GREP pode ser utilizado para encontrar padrões em arquivos de texto e exibir o número da linha. Por exemplo, se você deseja encontrar a palavra "teste" em um arquivo chamado `arquivo.txt` e exibir o número da linha, você pode utilizar o comando abaixo:
```bash
$ grep -n "teste" 3-GREP.md
```

### Usando o GREP para encontrar linhas que terminem com uma palavra específica
O GREP pode ser utilizado para encontrar linhas que terminem com uma determinada palavra. Por exemplo, se você deseja encontrar linhas que terminem com a palavra "linha" em um arquivo chamado `3-GREP.md`, você pode utilizar o comando abaixo:
```bash
$ grep "linha$" 3-GREP.md
```

### Usando o GREP para encontrar linhas que iniciem com uma palavra específica
O GREP pode ser utilizado para encontrar linhas que iniciem com uma determinada palavra 'linha', por exemplo. 
```bash
$ grep "^linha" 3-GREP.md
```

### Usando o GREP para encontrar linhas que iniciem com uma palavra específica e terminem com outra
O GREP pode ser utilizado para encontrar linhas que iniciem com uma determinada palavra 'Usando', por exemplo, e terminem com a palavra "específica". 
```bash
$ grep "^linha.*específica" 3-GREP.md
```

### Usando o GREP para encontrar padrões repetidos em arquivos
O GREP pode ser utilizado para encontrar padrões repetidos em arquivos de texto. Por exemplo, se você deseja encontrar a palavra "teste" repetida em um arquivo chamado `arquivo.txt`, você pode utilizar o comando abaixo:
```bash
$ grep -En "(que ){1,2}" 3-GREP.md
```
A opção `-E` permite que o GREP utilize expressões regulares estendidas. A opção `-n` permite que o GREP exiba o número da linha. A expressão regular `(que ){1,2}` indica que a palavra "que" deve ser repetida de 1 a 2 vezes.

Se quisermos contar quantas vezes a palavra "que" aparece em cada linha do arquivo, podemos usar o comando abaixo:
```bash
$ egrep -o "(que )+" 3-GREP.md | wc -l
```
A opção `-o` permite que o GREP exiba apenas o padrão encontrado. A expressão regular `(que )+` indica que a palavra "que" deve ser repetida uma ou mais vezes. O comando `wc -l` conta o número de linhas.


### Combinando comandos do GREP com o sed
O GREP pode ser combinado com o comando `sed` para realizar substituições em arquivos de texto. Por exemplo, se você deseja substituir a palavra "teste" pela palavra "exemplo" em um arquivo chamado `dados.csv`, você pode utilizar o comando abaixo:
```bash
$ sed "s/BRA/BR/g" dados.csv | grep -c "BR"
```
o exemplo acima substitui a palavra "BRA" pela palavra "BR" e conta quantas vezes a palavra "BR" aparece no arquivo.

## O comando CUT
O comando `cut` é um comando do sistema operacional Unix que é utilizado para extrair seções de linhas de arquivos de texto. Ele é muito útil para extrair informações de arquivos de texto, como por exemplo, extrair o nome de um usuário de um arquivo de log, ou para extrair dados de uma arquivo CSV. 

Considere o exemplo abaixo usando o arquivo `dados.csv`. Este aquivo conté as seguintes colunas: "Country Name","Country Code","Indicator Name","Indicator Code","1960","1961", ..., 2015. Queremos extrair o valor do indicador para o ano de 1960.
```bash
$ cut -d, -f1,4 dados.csv
```
O comando acima extrai as colunas 1 e 4 do arquivo `dados.csv`. A opção `-d,` indica que o delimitador das colunas é a vírgula. A opção `-f1,4` indica que as colunas 1 e 4 devem ser extraídas. Como este comando pode ser melhorado?

## Alternativas/Complementos ao GREP
O GREP é uma ferramenta poderosa para buscar padrões em arquivos de texto, mas existem outras ferramentas que podem ser utilizadas para realizar buscas em arquivos de texto. Alguns exemplos são o `awk` e o `sed`.

### O comando AWK
O comando `awk` é uma ferramenta poderosa para processar e analisar arquivos de texto. Ele é muito útil para extrair informações de arquivos de texto, como por exemplo, extrair o nome de um usuário de um arquivo de log, ou para extrair dados de uma arquivo CSV. O comando `awk` é composto por padrões e ações. Os padrões são expressões que indicam quando a ação deve ser executada, e as ações são comandos que são executados quando o padrão é satisfeito.

Considere o exemplo abaixo usando o arquivo `dados.csv`. Este arquivo contém as seguintes colunas: "Country Name","Country Code","Indicator Name","Indicator Code","1960","1961", ..., 2015. Queremos extrair o valor do indicador para o ano de 1960.
```bash
$ awk -F, '{print $1,$4}' dados.csv
```
O comando acima extrai as colunas 1 e 4 do arquivo `dados.csv`. A opção `-F,` indica que o delimitador das colunas é a vírgula. O comando `{print $1,$4}` indica que as colunas 1 e 4 devem ser impressas. 


### O comando `tr`
O comando `tr` é uma ferramenta poderosa para traduzir ou apagar caracteres em arquivos de texto. Ele é muito útil para substituir caracteres em arquivos de texto, como por exemplo, substituir acentos por caracteres sem acento, ou substituir espaços por tabs. O comando `tr` é composto por um conjunto de caracteres que indicam quais caracteres devem ser traduzidos ou apagados.

Considere o exemplo abaixo usando o arquivo `dados.csv`. Este arquivo contém as seguintes colunas: "Country Name","Country Code","Indicator Name","Indicator Code","1960","1961", ..., 2015. Queremos substituir a vírgula por um caracter ponto-e-vírgula. 

```bash
$ tr ',' ';' < dados.csv
```

O comando acima substitui a vírgula por um ponto-e-vírgula no arquivo `dados.csv`. O comando `<` indica que o arquivo `dados.csv` deve ser utilizado como entrada para o comando `tr`.

### O comando `cut`
O comando `cut` permite extrair seções de linhas de arquivos de texto. Ele é muito útil para extrair informações de arquivos de texto, como por exemplo, extrair o nome de um usuário de um arquivo de log, ou para extrair dados de uma arquivo CSV. O comando `cut` é composto por opções que indicam quais colunas devem ser extraídas.

Por exemplo, considere o arquivo `dados.csv`. Este arquivo contém as seguintes colunas: "Country Name","Country Code","Indicator Name","Indicator Code","1960","1961", ..., 2015. Queremos extrair as colunas 1 e 4 do arquivo `dados.csv` como fizemos anteriormente com o GREP.

```bash
$ cut -d, -f1,4 dados.csv
```

Os arquivos 1.text, 2.text e 3.text são verbetes do dicionário Histórico e Biográfico Brasileiro. o cabeçalho destes documentos contémo os seguintes campos: "title", "natureza", "sexo" e "cargo". Queremos extrair os campos do cabeçalho dos arquivos, com seus valores.




### o comando ripgrep
O [`ripgrep`](https://github.com/burntsushi/ripgrep) é uma alternativa ao `grep`. Ele é muito mais rápido que o `grep` e possui uma sintaxe mais amigável. Você pode instalar o `ripgrep` utilizando o gerenciador de pacotes da sua distribuição Linux. Por exemplo, no Ubuntu, você pode instalar o `ripgrep` utilizando o comando abaixo:
```bash
$ sudo apt install ripgrep
```

Explore o [tutorial do ripgrep](https://codapi.org/try/ripgrep/) para aprender mais sobre o `ripgrep`.



# Exercícios
1. Reproduza os exemplos acima no seu terminal, usando o ripgrep. e compare os tempos de execução.
2. Os arquivos 1.text, 2.text e 3.text são verbetes do dicionário Histórico e Biográfico Brasileiro. Use os comandos aprendidos acima para extrair os campos do cabeçalho dos arquivos.
