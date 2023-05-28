# Avaliação A2
Este documento inclui as instruções para a realização da avaliação A2 da disciplina de Introdução à Programação para Ciência de Dados.

## Forma da entrega
O trabalho deve ser feito em duplas. A entrega deve ser feita através do Eclass, na forma de um arquivo compactado (`.zip`) contendo os seguintes arquivos:
- Relatório em formato PDF, contendo o código fonte em LaTeX com os resultados gerados;
- Arquivo fonte `a2.py` com o código fonte em Python; para a geração dos resultados. Este arquivo deve conter uma variável global denominada `AUTORES = ['Nome1', 'Nome2']`, onde `Nome1` e `Nome2` devem ser substituídos pelos nomes dos integrantes da dupla;
- Arquivo de dados em  formato CSV ou Parquet, contendo os dados utilizados para a geração dos resultados. Este arquivo de dados deve corresponder a um anos de dados de um agravo de notificação do SINAN. O código para Download dos dados não precisar constar do arquivo fonte em formato `.py`.

## Questões
Para cada questão listada abaixo, uma função deve existir no arquivo fonte em formato `.py`. O nome da função deve ser o mesmo nome da questão, por exemplo: 
```python
def questao_1(datapath):
    # código da questão 1
    return resultado
```

A função deve receber como parâmetro o caminho para o arquivo de dados e retornar o resultado da questão. O arquivo fonte em formato `.py` deve conter um exemplo de uso de cada função.

1. Quantos registros existem no arquivo de dados?
2. Quantos registros existem por município?
3. Qual sexo possui mais registros?
4. Qual a idade média (em anos) dos registros?