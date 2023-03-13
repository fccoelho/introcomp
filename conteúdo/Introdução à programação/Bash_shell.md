# Introdução ao BASH
O [Bash](https://www.gnu.org/software/bash/manual/html_node/index.html) ou (Bourne again shell) é um ambiente de programação interativa utilizado para interação com o sistema operacional. É a linguagem de shell mais comumente utilizada no Linux. Seu nome é em homenagem à [Bourne Shell](https://pt.wikipedia.org/wiki/Bourne_shell) ou `sh`, primeira linguagem de script do ambiente UNIX criada por Stephen Bourne.

## Configurando o Bash
Como o BASH é utilizado para interagir com o SO, é muito comum utilizarmos um arquivo de configuração, o `.bashrc` para declarar variáveis de ambiente ou modificar o comportamento da shell. O `.bashrc` é apenas um script na própria linguagem shell, que é executado toda vez que o Bash é iniciado.

## Escrevendo e Executando scripts em Bash
Quando criamos um arquivo contendo um script BASH, é comum adicionarmos uma linha `SHEBANG`:
```bash
#!/usr/bin/env bash
```
esta linha, que deve ser a primeira linha do arquivo, diz ao SO qual a aplicação que deve executar este script.

## Sintaxe Básica
### Comentários
Usa-se o hashtag (#) para denotar que o restante da linha é um comentário:

```bash
# comentário
#### o número de hash tags não importa ####
x=10 # comentário é tudo que vem após o hashtag
```

### Variáveis
Variáveis são definidas por meio do sinal de `=`.

```
ano=2023
nome="flávio"
mensagem=Olá!
```

#### Variáveis Globais
Por padrão as variáveis são locais, ou seja só existem durante a execução do script. Para criar uma variável global, ou seja que persiste após a execução do script, usamos o comando `export`

```bash
export x=10
y=20
export y
```

### Estruturas de dados
#### Arrays

O Bash permite a criação de arrays que são basicamente listas de elementos. os elementos de uma array são representados por indices numéricos positivos.

```bash
lista=(1 2 3 4 5 34 65)
frutas[0]=banana
frutas[1]=abacaxi
echo $frutas # imprime primeiro elemento da array
echo ${frutas[1]} # imprime elemento 1
```

#### Arrays associativas
este é um tipo diferente de array também conhecido como dicionário. Nele os elementos da array são identificados por uma string ao invés de um simples número inteiro.

```bash
declare -A dicionario
dicionario["Brasil"]="Brasília"
dicionario["Goiás"]="Goiânia"
echo ${dicionario["Brasil"]}
```
Note que o `-A` deve ser maiúsculo, caso contrário estaremos declarando uma array normal.

#### Usando o `$`
A esta altura você já deve ter reparado que usamos o caracter `$` para recuperar o valor de uma variável. Mas não apenas para isso. Usá-lo em combinação com `()` e `{}`, irá retornar o resultado de uma operação:

```bash
var=$(expr 2 + 2) # aqui estamos executando o programa expr para calcular a soma
```
Podemos usar o operador `:=` ou `:-` para fornecer um valor default para a variável caso ela não tenha sido definida.

```bash
echo "${myname:=$(whoami)}"
myname=repolho
echo "${myname:=$(whoami)}"
```
No exemplo acima utilizamos o programa `whoami` que retorna o usuário.

Para apagar variáveis podemos usar o comando `unset`.

```bash
unset x
```

## Operações Aritméticas
Expressões aritméticas podem ser calculadas através do aplicativo `expr`

```bash
 expr 2 + 3
```

Note que os espaços são parte da sintaxe, neste caso.
Uma forma mais direta de fazer o mesmo (com ou sem espaços) é utilizando o `$` de uma nova maneira:

```bash
echo $((2**3))
```

Abaixo estão os operadores válidos.

operação | operador |
---------|-----------
soma  | +|
Subtração | - |
Multiplicação | * |
Divisão | / |
Exponenciação | ** | 
Resto da divisão | % |

