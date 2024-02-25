# Lista de exercícios de Python

## Tipos básicos
1. dada uma lista  de números aleatórios criada conforme o código abaixo:
   
```python
import random
lista = [random.randint(0, 15000) for i in range(500)]
```
com apenas uma linha de código, encontre quantos números distintos existem na lista.

1. No módulo `collections` do python existe uma classe chamada `Counter` que é um dicionário especial que conta a frequência de cada elemento de uma lista. Utilize essa classe para contar a frequência de cada elemento da lista acima.
2. Resolva o mesmo problema da questão anterior, mas agora utilizando o tipo defaultdict do módulo `collections`. 
3. Escreva um script que receba dois números como argumentos de linha de comando e imprima a soma deles.

## Funções

1. Escreva uma função que receba um número variável de argumentos e retorne a soma de todos eles.
2. Escreva um script que execute uma função `main` apenas quando é executado diretamente, mas não quando é importado como um módulo.
3. Escreva uma função que leia o arquivo [dados.csv](../dados.csv) e retorne uma lista de tuplas onde cada tupla é uma linha do arquivo. Cada elemento das tuplas é um dos elementos da linha separados por vírgulas. As 4 primeiras linhas do arquivo são comentarios e devem ser ignoradas. A quinta é o cabeçalho que deve ser tratada sem distinção das demais. 
