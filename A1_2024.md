# Trabalho complementar de A1

Crie um script na linguagem shell, para solucionar cada um dos problemas listados abaixo (um script por problema). A
entrega das suas soluções deve consistir em um único arquivo compactado em formato zip contendo todos os arquivos
necessários para avaliar as suas respostas. Não será possível adicionar novos arquivos após o envio.

## Problema 1:

Escreva um script para tornar executáveis apenas para o usuário e seu grupo, todos os scripts em um diretório, que
tiverem como primeira linha o seguinte:

```shell
#!/bin/bash 
```

### Resposta

```shell
#!/bin/bash 
for i in $(ls *.sh); do
    if [ $(head -n 1 $i) == "#!/bin/bash" ]; then
        chmod 770 $i
    fi
done
```

## Problema 2:

Utilizando o arquivo de texto `O_cortico.txt`, Romance de Aluísio Azevedo, escreva script shell que extraia do arquivo
os seguintes resultados (um por linha):

- Titulo do livro,
- quantidade de linhas, quantidade de palavras e quantidade de caracteres.
- Ano de Publicação do livro.

### Resposta

```shell
#!/bin/bash
echo "Titulo do livro: $(grep -m1 Title:  O_cortico.txt | cut -d: -f2)"
echo "Quantidade de linhas: $(wc -l O_cortico.txt | cut -d' ' -f1)"
echo "Quantidade de palavras: $(wc -w O_cortico.txt | cut -d' ' -f1)"
echo "Quantidade de caracteres: $(wc -m O_cortico.txt | cut -d' ' -f1)"
echo "Ano de Publicação do livro: $(grep -m1 publication: O_cortico.txt | cut -d, -f2)"
```

## Problema 3:

O Arquivo `palavras_antigas.lst` contém uma lista de palavras antigas da língua portuguesa. que ocorrem no texto do
arquivo `O_cortico.txt`. Escreva um script que conte o número de ocorrências de cada palavra do
arquivo `palavras_antigas.lst` no arquivo `O_cortico.txt`. salvando o resultado em um arquivo chamado `ocorrencias.txt`.
O arquivo `ocorrencias.txt` deve conter o nome da palavra e o número de ocorrências separados por um espaço em cada
linha.

### Resposta

```shell
#!/bin/bash
for i in $(cat palavras_antigas.lst); do
    echo "$i $(grep -o $i O_cortico.txt | wc -l)" >> ocorrencias.txt
done
```

## Problema 4:

O arquivo `O_cortico.txt` contém o texto do romance de Aluísio Azevedo, "O Cortiço". Escreva um script que conte o
número de ocorrências de cada palavra no arquivo `O_cortico.txt`. O script deve ignorar as palavras de tamanho menor que
4 caracteres e as palavras que começam com uma letra maiúscula. O resultado deve ser salvo em um arquivo
chamado `vocabulario.txt`. O arquivo `vocabulario.txt` não deve conter palavras repetidas e deve conter o nome da
palavra e o número de ocorrências separados por um espaço em cada linha.

### Resposta

```shell
#!/bin/bash
cat O_cortico.txt | tr -s ' ' '\n' | tr -d '[:punct:]' | tr '[:upper:]' '[:lower:]' | grep -v '^.\{1,3\}$' | grep -v '^[A-Z]' | sort | uniq -c | sort -nr | awk '{print $2, $1}' > vocabulario.txt
```

Alternativa:

```shell
#!/bin/bash
cat O_cortico.txt | tr -s ' ' '\n' | tr -d '[:punct:]' | tr '[:upper:]' '[:lower:]' | grep -v '^.\{1,3\}$' | grep
-v '^[A-Z]' | sort | uniq -c | sort -nr > temp.txt
while read line; do
count=$(echo $line | cut -d' ' -f1)
word=$(echo $line | cut -d' ' -f2-)
echo "$word $count"
done < temp.txt > vocabulario.txt
rm temp.txt
```

## Problema 5:

Crie um script em Bash que receba um número inteiro (n) como argumento, e produza um arquivo HTML contendo uma tabela mostrando as n palavras mais frequentes calculadas no Problema 4. Dica: crie manualmente as partes de do HTML que não dependem dos dados, em dois arquivos: início.html e fim.html. Construa as linhas da tabela de forma programática, e depois junte tudo em um arquivo final chamado palavras.html.

### Resposta

```shell
#!/bin/bash
n=$1
echo "<table>" > palavras.html
echo "<tr><th>Palavra</th><th>Quantidade</th></tr>" >> palavras.html
head -n $n vocabulario.txt | while read line; do
    word=$(echo $line | cut -d' ' -f1)
    count=$(echo $line | cut -d' ' -f2)
    echo "<tr><td>$word</td><td>$count</td></tr>" >> palavras.html
done
echo "</table>" >> palavras.html
```

## Bônus (1 ponto): 
Pinte de vermelho as linhas da tabela correspondentes a palavras antigas, listadas em palavas_antigas.lst.

### Resposta

```shell
#!/bin/bash
n=$1
html="palavras_red.html"
echo "<table>" > $html
echo "<tr><th>Palavra</th><th>Quantidade</th></tr>" >> $html
head -n $n vocabulario.txt | while read line; do
    word=$(echo $line | cut -d' ' -f1)
    count=$(echo $line | cut -d' ' -f2)
    if grep -q $word palavras_antigas.lst; then
        echo "<tr style='color:red'><td>$word</td><td>$count</td></tr>" >> $html
    else
        echo "<tr><td>$word</td><td>$count</td></tr>" >> $html
    fi
done
echo "</table>" >> $html
```
