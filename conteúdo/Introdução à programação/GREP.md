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
$ grep "teste" GREP.md
```
Um exemplo mais avançado é buscar por linhas que não contém a palavra "teste" em um arquivo chamado `GREP.md`:
```bash
$ grep -v "teste" GREP.md
```

### Usando o GREP para encontrar padrões em arquivos e exibir o número da linha
O GREP pode ser utilizado para encontrar padrões em arquivos de texto e exibir o número da linha. Por exemplo, se você deseja encontrar a palavra "teste" em um arquivo chamado `arquivo.txt` e exibir o número da linha, você pode utilizar o comando abaixo:
```bash
$ grep -n "teste" GREP.md
```

### Usando o GREP para encontrar linhas que terminem com uma palavra específica
O GREP pode ser utilizado para encontrar linhas que terminem com uma determinada palavra. Por exemplo, se você deseja encontrar linhas que terminem com a palavra "linha" em um arquivo chamado `GREP.md`, você pode utilizar o comando abaixo:
```bash
$ grep "linha$" GREP.md
```

### Usando o GREP para encontrar linhas que iniciem com uma palavra específica
O GREP pode ser utilizado para encontrar linhas que iniciem com uma determinada palavra 'linha', por exemplo. 
```bash
$ grep "^linha" GREP.md
```

### Usando o GREP para encontrar linhas que iniciem com uma palavra específica e terminem com outra
O GREP pode ser utilizado para encontrar linhas que iniciem com uma determinada palavra 'Usando', por exemplo, e terminem com a palavra "específica". 
```bash
$ grep "^linha.*específica" GREP.md
```

### Usando o GREP para encontrar padrões repetidos em arquivos
O GREP pode ser utilizado para encontrar padrões repetidos em arquivos de texto. Por exemplo, se você deseja encontrar a palavra "teste" repetida em um arquivo chamado `arquivo.txt`, você pode utilizar o comando abaixo:
```bash
$ grep -En "(que ){1,2}" GREP.md
```
A opção `-E` permite que o GREP utilize expressões regulares estendidas. A opção `-n` permite que o GREP exiba o número da linha. A expressão regular `(que ){1,2}` indica que a palavra "que" deve ser repetida de 1 a 2 vezes.

