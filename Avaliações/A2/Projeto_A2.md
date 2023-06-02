# Avaliação A2
Este documento inclui as instruções para a realização da avaliação A2 da disciplina de Introdução à Computação para Ciência de Dados.

## Forma da entrega
O trabalho deve ser feito em duplas. A entrega deve ser feita através do Eclass, na forma de um arquivo compactado (`.zip`) contendo os 3 seguintes arquivos:
- **Relatório em formato PDF**, juntamente com o seu código fonte em LaTeX com os resultados gerados; O relatório deve também conter uma breve explicação sobre o que foi feito em cada função e como foi feito;
- **Arquivo fonte** `a2.py` com o código fonte em Python; para a geração dos resultados. Este arquivo deve conter uma variável global denominada `AUTORES = ['Nome1', 'Nome2']`, onde `Nome1` e `Nome2` devem ser substituídos pelos nomes dos integrantes da dupla;
- **Arquivo de dados** em  formato CSV ou Parquet, contendo os dados utilizados para a geração dos resultados. Este arquivo de dados deve corresponder a um anos de dados de um agravo de notificação do SINAN. O código para Download dos dados não precisar constar do arquivo fonte em formato `.py`.

## Questões
Para cada questão listada abaixo, uma função deve existir no arquivo fonte `a2.py`. O nome da função deve ser o mesmo nome da questão, por exemplo: 
```python
def questao_1(datapath):
    # código da questão 1
    return resultado
```

A função deve receber como parâmetro o caminho para o arquivo de dados e retornar o resultado da questão. 

1. Quantos registros existem no arquivo de dados? O resultado deve ser um número inteiro.
2. Quantos registros existem por município? a função deve retornar uma série do pandas (pd.Series)
3. Qual sexo possui mais registros? Retorne uma tupla com o sexo mais numeroso e um dicionário tendo como chaves 'M' e 'F' para os sexos con a contagem de registros em cada sexo.
4. Qual a idade média (em anos) dos registros? retorne um float
5. a coluna `SG_UF_NOT` contém a sigla (string, por exemplo 33: 'RJ') da unidade federativa. Qual a unidade federativa com mais registros? Retorne o resultado como um dicionário tendo como chaves as siglas das unidades federativas e a quantidade de registros.
6. Novamente usando a coluna `SG_UF_NOT`, qual a unidade federativa com mais registros de pessoas do sexo masculino? Retorne o resultado como um dicionário tendo como chaves as siglas das unidades federativas e a quantidade de registros.
7. Descubra quantos municípios existem em cada unidade federativa (UF) (busque no google). determine, para a sua tabela de dados, que proporção dos munícípios de cada UF, tem pelo menos um registro. Retorne o resultado como um dicionário tendo como chaves as siglas das unidades federativas e a proporção de municípios com pelo menos um registro. 
8. Usando o comando `pd.to_datetime` do Pandas, crie uma nova coluna chamada `DT_NOTIFICACAO` com o tipo `datetime64[ns]` a partir da coluna `DT_NOTIFIC`, e uma coluna `DT_SINTOMAS` também de tipo `datetime64[ns]`. A partir destas duas novas colunas calcule o número de dias de atraso entre os sintomas e a notificação e salve em uma coluna `ATRASO_NOT`. Retorne um dataframe com as colunas `DT_NOTIFICACAO`,`DT_SINTOMAS` e `ATRASO_NOT`.
9. Calcule a média e desvio padrão do atraso de notificação por unidade federativa. Retorne o resultado como um dicionário tendo como chaves as siglas das unidades federativas e a média e desvio padrão do atraso de notificação. Exemplo: `{'RJ': (média, desvio padrão),...}`.
10. Calcule a média do atraso de notificação por município. Plote o número de notificações (eixo x) contra o atraso médio (eixo y) em cada município como um scatter plot. Retorne o resultado como uma séries do Pandas com as médias por município.

## Critérios de correção
Caso o código de alguma função apresentar erros que impeçam a sua execução, esta receberá pontuação 0. O código de cada função será avaliado independentemente. Questões podem receber crédito parcial, caso seu código não contenha bugs mas o resultado esperado esteja errado. O crédito parcial fica a critério do professor. 

Use o módulo de teste test_a2.py para verificar se a formatação e a sintaxe da sua entrega estão corretas. O teste **não irá corrigir** as respostas. Para executar o teste, execute o comando `pytest test_a2.py` no diretório onde se encontra o arquivo `test_a2.py`.
