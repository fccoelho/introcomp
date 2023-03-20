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

## Laços
A linguagem shell como qualquer linguagem que se preze possui construtos para realizar operações em laços de repetição.

Os comandos abaixo executam os comandos dentro do laço até que a condição de execução retorne `0`, ou o comando `break` ocorra. Caso seja necessário saltar uma execução o comando `continue` pode ser utilizado também.

### until
O comando `until` executa os comandos dentro do laço até que a condição de execução retorne `0` ou se torne verdadeira.

Note que abaixo, o `-eq` significa "é igual a".
```bash
x=0
until [ $x -eq 10 ]; do
    echo $x
    x=$((x+1))
done
```
Agora é um bom momento para explorar os operadores de comparação do bash:

operador|sgnificado|exemplo
--------|----------|-------
-eq | igual a | [ $x -eq 10 ]
-ne | diferente de | [ $x -ne 10 ]
-gt | maior que | [ $x -gt 10 ]
-ge | maior ou igual a | [ $x -ge 10 ]
-lt | menor que | [ $x -lt 10 ]
-le | menor ou igual a | [ $x -le 10 ]
< | menor que (com parenteses duplos) | (($x < 10))
\> | maior que (com parenteses duplos) | (($x > 10))
<= | menor ou igual a (com parenteses duplos) | (($x <= 10))
\>= | maior ou igual a (com parenteses duplos) | (($x >= 10))
!= | diferente de (com parenteses duplos) | (($x != 10))

### while 
O laço `while` executa os comandos dentro do laço enquanto a condição de execução retornar `0` ou seja verdadeira.

```bash
$ while test-commands; do consequent-commands; done
```

### for
O laço `for` executa os comandos dentro do laço para cada elemento de uma lista.
```bash
frutas=(banana abacaxi uva)
for fruta in ${frutas[@]};
do 
    echo $fruta 
done
```

## Condicionais
No bash podemos utilizar os comandos `if`, `elif` e `else` para executar comandos condicionalmente.
### if
A clausula `if` executa os comandos dentro do laço se a condição de execução retornar `0` ou for verdadeira.
```bash
x=1
if [ $x -eq 1 ]; then
    echo "x é igual a 1"
fi
```

### if-else
A clausula `if-else` executa os comandos dentro do laço se a condição de execução retornar `0` ou for verdadeira. Caso contrário, executa os comandos dentro do `else`.

```bash
x=1
if [ $x -eq 5 ]; then
    echo "x é igual a 5"
else
    echo "x é diferente de 5"
fi
```

### elif
A clausula `elif` executa os comandos dentro do laço se a condição de execução retornar `0` ou for verdadeira. Caso contrário, executa os comandos dentro do `elif` seguinte.

```bash
x=1
if [ $x -eq 5 ]; then
    echo "x é igual a 5"
elif [ $x -eq 4 ]; then
    echo "x é igual a 4"
elif [ $x -eq 3 ]; then
    echo "x é igual a 3"
elif [ $x -eq 2 ]; then
    echo "x é igual a 2"
else
    echo "x é diferente de 5, 4, 3 e 2"
fi
```
