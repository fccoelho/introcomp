# Lista de Exercícíos sobre Numpy e Pandas
Nesta lista de exercícios vamos explorar estas duas bibliotecas que são muito utilizadas para manipulação de dados em Python.

## Numpy

1. Crie um array com 10 elementos usando a função arange
2. Transforme esse array de 1D (1x10) para 2D (2x5) usando a função reshape
3. Crie duas matrizes bidimensionais com valores aleatórios
4. calcule a transposta de cada matriz
5. multiplique as duas matrizes
6. Salve as matrizes de entrada e a de saída em arquivos. Qual o tamanho dos arquivos gerados?
7. Crie um vetor (array unidimensional) cujos valores sejam o resultado da função $f(x) = 3x^2 - 2x +7$ para cada valor de x em um vetor dado com 1000 elementos, construído com linspace.
8. Encontre uma maneira de calcular numericamente a primeira derivada da função acima, e construa um plot com as duas funções: A derivada calculada numericamente e a derivada analítica de $3x^2 - 2x +7$.
9. O índice de massa corporal $IMC=peso/altura^2$ é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta. construa uma array com 100 os valores de altura entre 150cm a 195cm, e  100 valores de peso entre 50kg e 100kg. Calcule o IMC para todas as valores e construa uma matriz 2D com os valores de IMC. 

## Pandas
1. Crie um dataframe com 4 colunas e 400 linhas, sem usar loops.
2. Renomeie as colunas deste dataframe.
3. Extraia a array correspondente aos dados no Dataframe
4. Adicione as 4 colunas criando uma nova coluna com a resposta
5. Usando Pandas, calcule a média por coluna do dataframe
6. Usando Pandas, calcule a média por linha do dataframe
