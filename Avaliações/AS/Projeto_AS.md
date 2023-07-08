# Avaliação AS
Este documento inclui as instruções para a realização da avaliação AS da disciplina de Introdução à Computação para Ciência de Dados.

## Forma da entrega
O trabalho deve ser feito **individualmente**. A entrega deve ser feita através do Eclass, na forma de um arquivo compactado (`.zip`) contendo os 3 seguintes arquivos:

- **Relatório em formato PDF**, juntamente com o seu código fonte em LaTeX com os resultados gerados; O relatório deve também conter uma breve explicação sobre o que foi feito em cada função e como foi feito;
- **Arquivo fonte** `AS.py` com o código fonte em Python; para a geração dos resultados. 
    - **Este arquivo deve conter uma variável global denominada `AUTOR = 'Nome'`**, onde `Nome` deve ser substituído pelo seu nome;
    - **Deve conter ainda uma segunda variável global `DADOS`**, indicando o nome do arquivo de dados, por exemplo: `DADOS = 'malaria.csv'.
- **Arquivo de dados** em  formato CSV ou Parquet, contendo os dados utilizados para a geração dos resultados. Este arquivo de dados deve corresponder a um anos de dados de um agravo de notificação do SINAN. O código para Download dos dados não precisa constar do arquivo fonte em formato `.py`.

## Questões
Para cada questão listada abaixo, uma função deve existir no arquivo fonte `as.py`. O nome da função deve ser o mesmo nome da questão, por exemplo: 
```python
def questao_1(datapath=DADOS):
    # código da questão 1
    return resultado
```

1. Quantas colunas de dados existem no arquivo de dados? retorne um número inteiro.
2. Liste os tipos de dados mais adequados para cada coluna do Dataframe e converta cada coluna para o tipo escolhido. Justifique a sua escolha, no relatório. A função deve retornar o Dataframe com as colunas convertidas. Você pode usar a função `SINAN.metadata_df("doença escolhida")` para obter os metadados da doença escolhida, e basear sua conversão das colunas na explicação do significado de cada coluna.
3. Quais variáveis do dataframe, podem ser tratadas como variáveis categóricas, ou seja, que podem assumir um número finito de valores (sem ordenação intrínseca)? Liste estas variáveis e converta-as para o tipo `category`. A função deve retornar o Dataframe com as colunas convertidas. Justifique sua escolha das variáveis categóricas no relatório.
4. O método `info()` do Dataframe, retorna o número de valores "não nulos" em cada coluna, e o número total de linhas no dataframe. Você concorda com o número de "não nulos" nas várias colunas? Quando houver discrepância entre a sua conclusão e o resultado retornado por `info()`, explique porque isto ocorre. A função deve retornar um dicionário com o nome da coluna e o número de valores não nulos, segundo sua análise em cada coluna. Preencha os valores faltantes com o valor `pd.NA` (onde `pd` é a biblioteca pandas).
5. Como você faria para salvar o Dataframe em um arquivo, de forma que ele possa ser lido novamente, **sem perda de informação sobre os tipos**? Implemente a sua solução, salve o datframe com os tipos definidos, A função deve retornar o Dataframe lido deste arquivo.

## Critérios de correção
Caso o código de alguma função apresentar erros que impeçam a sua execução, esta receberá pontuação 0. O código de cada função será avaliado independentemente. Questões podem receber crédito parcial, caso seu código não contenha bugs mas o resultado esperado esteja errado. O crédito parcial fica a critério do professor.
