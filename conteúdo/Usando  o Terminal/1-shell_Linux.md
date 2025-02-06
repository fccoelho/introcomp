# O Shell do Linux
O Shell (casca, em inglês), é o mais próximo que conseguimos chegar de manipular o SO. É uma interface textual para controle do seu computador.

A comunicação por text na era digital domina todas as outras formas de comunicação, pensem em quantas mensagens de texto uma pessoa média envia e recebe por dia. Por quê então tão poucas pessoas se comunicam com os seus computadores por mensagens de texto?

A resposta mais direta a esta pergunta pode ser: "porquê não sabe a lingua do computador". E isto é verdade. Por isso iremos aprender nesta aula a como nos comunicar por texto com o computador.

Uma outra razão para não nos comunicarmos mais por texto é a Insistência dos designers de interface para que utilizemos interfaces gráficas. Mas veremos que para muitas tarefas a interface de texto pode ser muito mais eficiente.

O shell do Linux, também chado de *terminal* ou *console*, consiste basicaent de uma linha em branco na qual podemos digitar nomes de aplicativos, usar comandos do SO (também intermediados por aplicativos), e construir peuenos trechos de código na linguagem Shell para executa tarefas mais complexas para as quais precisariamos combinar as capacidades de vários aplicativos.

## Abrindo um terminal ou console
No Linux para ter acesso ao terminal, basta procurar no menu de aplicativos pela palavra `terminal` ou `console`. Geralmente esta busca trará mais de uma alternativa de aplicativos de terminal.

Escolha um e execute. Se você está acompanhando esta aula de uma máquina com Windows, simplesmente abra o GitBash ele é uma shell do Linux quase completa. Geralmente o atalho de teclado `ctrl-alt-t` abrirá o terminal padrão. Sim, usuários de terminal preferem sempre usar o teclado do que o mouse!

A primeira coisa que chamará a sua atenção é o chamado **prompt** qe será parecido com o da figura abaixo:
![prompt](prompt.png)

O terminal parece saber qual o seu nome de usuário e o nome do seu computador. Isto nos informa que cada sessão do terminal está associada a um usuário e pode estar conectada a outro computador, caso contrário não precisaria informar o nome do computador.

O console tipicamente se inicial na pasta do usuário denotada por `~`, no prompt. A qualquer momento você podesaber em que diretório (o mesmo que pasta) você está, usando o comando `pwd`(print working directory).
![pwd](pwd.png)

Tudo que escrevemos no terminal do Linux é sensível à capitalização, ou seja, o comando "Pwd" ou "PWD" não existe.

O console está sempre localizado em um diretório da árvore do sistema de arquivos. Daí a importância de sabermos qual o "diretório de trabalho" atual. A qualquer momento  podemos retornar à pasta do usuário digitando `cd ~` ou apenas `cd`.

O sistema de arquivos do Linux consiste em uma árvore de diretórios  com uma única raiz. Experimente os seguintes comando:
```bash
$ cd /
$ pwd
```

Caso vc queira visualizar esta árvore, ou o ramo que começa no diretório em que você está, pode usar o seguinte comando:

```bash
$ tree
```

A esta altura você já percebeu que o comando `cd` significa "change directory". Se você executou o comando `cd /` acima, pode agora digitar os seguintes comandos:

```bash
$ cd home
$ pwd
```

**Quiz:**

    Se você estiver em seu diretório, `/home/<username>` como você pode mudar para o diretório `home` com um só comando?

Para saber o nome do usuário local (no caso de não aparecer no seu prompt), você pode usar o comando `whoami`.

## Criando diretórios

Outra tarefa muito fácil de se realizar no terminal é criar diretórios:

```bash
$ mkdir /tmp/novodir
$ cd /tmp/novodir
```

Note que aqui utilizamos um caminho "absoluto", ou seja que começa da raiz do arquivo.

 Você pode criar múltiplos diretórios de uma vez, caso queira:

 ```bash
 $ mkdir dir1 dir2 dir3
 ```

 Ou podemos criar um ramo de diretórios de uma só vez:

 ```
 $ mkdir -p dir4/dir5/dir6
 $ tree
 ```

Ao manipular diretórios podemos usar alguns atalhos para evitar ter de escrever os nomes dos diretórios. Por exemplo, `.` representa o diretório atual. O diretório acima do atual, é denotado por `..`. 

**Quiz:**

    Vá para o diretório `dir6` criado anteriormente (usando `cd`), e volte para o diretório `/tmp/novodir` apenas usando atalhos.

## Criando Arquivos

Outra tarefa comum realizada no terminal é a manipulação de arquivos. Por exemplo podemos criar um arquivo com a listagem do conteúdo do diretório corrente:
![ls_arquivo](ls.png)

O que fizemos acima foi apenas redirecionar a saída do comando `ls`para o arquivo `lista.txt`. Em seguida usamos o comando `cat` para mostrar na tela o conteúdo do arquivo.

**Quiz:**

    Duplique o conteúdo de lista.txt, em um outro arquivo chamado 'duplicado.txt' com um único comando.

A resposta do quiz acima é:
```bash
$ cat lista.txt lista.txt > duplicado.txt
```
o operador `>` cria um novo arquivo, ou caso já exista um de mesmo nome, o sobrescreve.

Para adicionar mais conteúdo a um arquivo, podemos usar um outro operador:

```bash
$ echo "primeira linha" > multi.txt
$ echo "segunda linha" >> multi.txt
$ echo "terceira linha" >> multi.txt
```
Use `cat` para verificar o conteúdo de `multi.txt` após a execução dos comandos acima. 

## Movendo e manipulando arquivos

Mover arquivos de um ponto a outro na árvore de diretórios pode ser feito com o comando `mv`

```bash
$ mv duplicado.txt dir1/
$ ls dir1
```
O comando acima move o arquivo `duplicado.txt` para o diretório `dir1`. Para desfazer o movimento, uma possibilidade é

**Quiz**

    Mova o arquivo `duplicado.txt` de volta para o diretório corrente.

O comando `mv` aceita mais de um argumento então se passarmos mais de um nome a ele o último será interpretado como o destino.

```bash
$ mv dir1 multi.txt dir4/dir5/dir6
$ ls dir4/dir5/dir6
$ tree
```
O comando `mv` move arquivos e diretórios. Caso queiramos apenas copiar, ou seja, criar uma cópia de um arquivo sem apagar a versão original, temos que usar o comando `cp`.

```bash
$ cp dir4/dir5/dir6/dir1/duplicado.txt .
$ ls dir4/dir5/dir6/dir1
$ ls
```
O comando  `cp` permite renomear a copia que estamos fazendo.

```bash
$ cp duplicado.txt duplicado_copia.txt
$ ls
```
## Apagando Arquivos e diretórios

Para apagar arquivos usamos o comando `rm`.

**Este comando é muito perigoso pois não há como recuperar arquivos que foram apagados**

```bash
$ rm duplicado_copia.txt
$ ls
```
O comando `rm`só apaga arquivos e não diretórios. Para apagar diretórios vc precisa do comando `rmdir` mais ele só apaga diretórios vazio. Para apagar uma ramo inteiro:

```bash
$ rm -r dir4
$ ls
```

## Conectando comandos: introdução aos pipes.
Todos os programas no Linux possuem [entradas e saídas padrão](https://en.wikipedia.org/wiki/Standard_streams). Elas são chamadas de STDIN e STDOUT, respectivamente. Então torna-se possível conetar a saída de um programa com a entrada de outro através de tubo ou "pipes" no jargão do Linux. 

Suponha que você deseja saber quantos arquivos existem no seu diretório home. O comando `wc` (word count) faz a contagem:

```bash
$ wc -l multi.txt
```
usando a opção `-l` o `wc` nos retorna a contagem de linhas.

Então poderíamos resolver nossa tarefa com três comandos:

```
ls ~ > file_list.txt
wc -l file_list.txt
rm file_list.txt
```
Este método funciona, mas requer a criação de um arquivo temporário para conter o conteudo do diretório, que tem que ser deletado após a contagem.

Para simplificar esta solução precisamos saber que todos os processos no Linux possuem entradas e saídas padrão. Elas são chamadas de STDIN e STDOUT, respectivamente. Então torna-se possível conetar a saída de um programa com a entrada de outro através de tubo ou "pipes" no jargão do Linux.

```bash
$ ls ~ | wc -l
```

O tubo é representado pelo caracter `|`, e desta forma não há necessidade de criar uma arquivo temporário.

Podemos utilizar o pipe para quanquer tarefa, por exemplo apenas para visualizar texto, por exemplo:

```bash
$ ls /etc | less
```
Pressione a tecla *q* para sair do less.

Podemos usar multiplos pipes também

```bash
cat duplicado.txt | uniq | wc -l
```

este "pipeline" conta quantas linhas distintas existem em duplicado. Curiosamente o resultado obtido está errado! Para sabermos o porquê precisamos consulta o manual de `uniq`

```bash
$ man uniq
```
![man](man.png)

Ah... então o `uniq` só detecta linhas duplicadas se elas forem adjacentes! sem problema!

```bash
$ sort duplicado.txt | uniq | wc -l
```

A esta altura você já advinhou o que faz o comando `sort`, mas se ainda estiver com dúvidas pode usar o `man` para descobrir!

No exemplo acima passamos um arquivo para o programa sort abrir. Digamos que temos um outro arquivo em nosso diretório, chamado `lista_de_compras.txt`

```bash
$ cat lista_de_compras.txt
óleo
azeite
Biscoito 
banana
```

a outra maneira de ordenar nossa lista é:

```bash
$ sort < lista_de_compras.txt
```
Neste caso o operador `<` estáenviando o conteúdo do arquivo para a `STDIN` do programa `sort`. Como de costume a `STDOUT` continua direcionada para o terminal.

**Quiz:**

    Experimente estender a pipeline com outros comando que você já aprendeu. Por exemplo: qual a resposta deste comando: 'sort -r lista_de_compras.txt | head -1' ?

## Permissões de Arquivos
O controle de acesso a arquivos no Linux se dá em três níveis: *dono*, *grupo*, e *outros*. Estas permissões são codificadas em uma string de 10 caracteres, que podemos ver quando usamos o comando `ls -l`

```bash
$ ls -l
total 4
-rw-rw-r-- 1 fccoelho fccoelho 30 mar 16 13:29 lista_de_compras.txt
```
O primeiro caracter pode ser `d` se o nome for um diretório ou `-` se for um arquivo (existem outras possibilidades também). Os 9 caracteres seguintes devem ser lidos em grupos de 3:

dono|grupo|outros
----|-----|------
rwx|rwx|rwx

o primeiro caracter de cada trinca diz se a leitura é permitida: `r`, ou não: `-`. O segundo diz se a escrita é permitida: `w`, ou não: `-` e o terceiro diz se o arquivo é executável: `x` ou não:`-`. Sumarizando:
![permissões](permissions.png)

cada possibilidade de permissão pode ser representada em notação numérica octal, mais compactas, como ilustrado na tabela acima.

Para alterar as pemissões de arquivos usanmos o comando `chmod`. Apenas o dono do arquivo ou diretório pode mudar suas permissões.
```bash
$ chmod --help
Usage: chmod [OPTION]... MODE[,MODE]... FILE...
  or:  chmod [OPTION]... OCTAL-MODE FILE...
  or:  chmod [OPTION]... --reference=RFILE FILE...
Change the mode of each FILE to MODE.
With --reference, change the mode of each FILE to that of RFILE.

  -c, --changes          like verbose but report only when a change is made
  -f, --silent, --quiet  suppress most error messages
  -v, --verbose          output a diagnostic for every file processed
      --no-preserve-root  do not treat '/' specially (the default)
      --preserve-root    fail to operate recursively on '/'
      --reference=RFILE  use RFILE's mode instead of MODE values
  -R, --recursive        change files and directories recursively
      --help     display this help and exit
      --version  output version information and exit

Each MODE is of the form '[ugoa]*([-+=]([rwxXst]*|[ugo]))+|[-+=][0-7]+'.
```

**Exemplos:**

1. `chmod a+x <arq>`: Dá acesso de leitura a todos os usuários.
2. `chmod +r <arq>`: O mesmo que acima
3. `chmod og-x <arq>`: Retira permissões de execução de usuários que não sejam o dono.
4. `chmod u+rwx <arq>`: Dá todas as permissões ao dono.
5. `chmod o-rwx <arq>`: Retira todas as permissões de usuários que não sejam o dono ou pertençam ao grupo do arquivo. 

## Links
No sistema de arquivos do Linux todos os arquivos e diretórios possuem um identificador numérico chamado número do **inode**. Podemos descobrir este número facilmente
```bash
$ touch foo
$ ls -i foo
21191 foo
```
### Links rígidos
 Um link permite darmos mais de um nome a um mesmo arquivo. Podemos criar links com o comando `ln`

 ```bash
 $ ln foo bar
 ```
 o comando acima cria um um link chamado `bar` para o arquivo `foo`. Verifique agora os seus respectivos números de **inode**. Eles possuem o mesmo número pois correspondem ao mesmo arquivo. 

 **Quiz:**

    Apague o arquivo `foo`. O que acontece com `bar`?

Existem muitas outras pérolas no console do Unix. Seguem algumas referências abaixo.


### Links Simbólicos
O segundo tipo de link também conhecido como `symlink`, é criado com o comando `ln -s`.

**Quiz:**

    Crie um link symbólico e investigue suas propriedades.

## Manipulando Textos
A manipulação de textos é uma tarefa muito comum para Cientistas de dados. Existem comandos na shell do Linux extremamente poderosos para manipulação de textos:

### O editor **sed**
O acrônimo `sed` significa "stream editor" ou seja ueditor de fluxos de texto. Mas o qu significa isso? Basicamente significa que é um editor desenhoado para processar uma sequência de dados textuais de tamanho arbitrário, e mais importante de maneira não interativa.

para entender o `sed` vamos precisar de um texto.

```bash
$ wget https://github.com/Illumina/licenses/raw/master/Simplified-BSD-License.txt > BSD.txt
```

O `sed` é invocado da seguinte maneira: `sed [opções] comandos <arq. de entrada>`

Vamos ver alguns exemplos:
```bash
$ sed '' BSD.txt
Copyright (c) 2010-2015 Illumina, Inc.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIEDi
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
Se não especificarmos nenhum comando, o texto sai pelo `STDOUT` do `sed` como entrou. Podemos também entregar o texto ao `sed` via `STDIN`.

```bash
$ cat BSD.txt | sed 'p' 
Copyright (c) The Regents of the University of California.
Copyright (c) The Regents of the University of California.
All rights reserved.
All rights reserved.


Redistribution and use in source and binary forms, with or without
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
modification, are permitted provided that the following conditions
are met:
are met:
. . .
```
O comando `p` significa print, então para cada linha o sed a imprime, mas como tudo que entra também sai, as linhas terminas saindo duplicadas Para evitar esta duplicação basta colocar a opção `-n`: `sed -n 'p' BSD.txt`. A esta altura você já percebeu que o `sed` trabalha linha a linha.

```bash
$ sed -n '1,5p' BSD.txt
Copyright (c) 2010-2015 Illumina, Inc.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
```
Aqui especificamos que o comando deve ser aplicado aenas às linhas de 1 a 5.

podemos também especificar linhas alternadas:

```bash
$ sed -n '1~2p' BSD.txt > 2em2.txt
```
**Quizz:**

    Modifique o comando acima, para retornar as linhas que foram omitidas. Dica: troque o comando `p` por `d`.

Note que o sed não está modificando o arquivo de entrada, apenas retornando o resultado da sua transformação no terminal. Mas é possível pedir que ele edite diretamento no arquivo original, usando a opção `-i`. Porém devemos usar esta opção **com cuidado**, pois as alterações são **irreversíveis!**. Felizmente o sed nos dá a opção de criarmos um backup neste caso:

```bash
$ sed -i.bak '1~2d' 2em2.txt
```
 experimente!

Um dos usos mais comuns do `sed` é para substituir strings. Por exemplo

```bash
$ sed 's/copyright/copyleft/' < BSD.txt
```
Este comando entretanto apenas substitui a primeira ocorrência da palavra buscada em cada linha. Para substituir todas as ocorrências:

```bash
$ sed 's/copyright/copyleft/g' < BSD.txt
```
Se você quisesse substituir apenas a segunda ocorrência da palavra em cada linha, bastaria trocar o `g` por *2*.

para mostrar apenas as linhas onde a substituição foi feita:

```bash
$ sed -n 's/copyright/copyleft/gp' < BSD.txt
```
mas o nosso *script* não substituiu as ocorrências de "COPYRIGHT" devido à sensibilidade à capitalização. Sem problemas:
```bash
$ sed -n 's/copyright/copyleft/gip' < BSD.txt
```
Buscas mais complexas podem empregar *expressões regulares* que fogem ao escopo desta aula.

## Referências

1. https://en.wikipedia.org/wiki/Pipeline_(Unix)
2. https://www.debian.org/doc/manuals/debian-reference/ch01.en.html
3. https://tldp.org/LDP/gs/node5.html
   



