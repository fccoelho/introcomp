# Analizando dados de Saúde
A bilioteca PySUS é uma ferramenta que permite a extração de dados do DataSUS, o departamento de informática do SUS. O DataSUS é responsável por armazenar e disponibilizar dados sobre a saúde pública no Brasil. A biblioteca PySUS permite a extração de dados de diversos bancos de dados do DataSUS. Um destes bancos chama-se SINAN, que é o Sistema de Informação de Agravos de Notificação. O SINAN é responsável por armazenar dados sobre doenças de notificação compulsória, ou seja, doenças que devem ser notificadas ao Ministério da Saúde. Neste projeto, vamos analisar os dados de dengue no Brasil. Para isso, vamos utilizar a biblioteca PySUS para extrair os dados do SINAN e, em seguida, vamos utilizar a biblioteca Pandas para analisar os dados extraídos.

## Instalação da biblioteca PySUS
Para instalar a biblioteca PySUS, basta executar o comando abaixo no terminal:
```bash
pip install PySUS
```
Vamos também instalar a biblioteca Pandas, que utilizaremos mais adiante:
```bash
pip install pandas
```

## Introdução ao uso da biblioteca PySUS
A documentação da biblioteca PySUS pode ser encontrada neste [link](https://pysus.readthedocs.io/pt/latest/).

Para começar a interagir com o banco do SINAN, podemos listar os agravos de notificação disponíveis no banco de dados. Para isso, basta executar o código abaixo:
```python
from pysus.online_data import SINAN
import pandas as pd
SINAN.list_diseases()
```
Para maiores informações sobre o uso da biblioteca PySUS, consulte a documentação.

## Escolhendo um agravo de notificação
A partir da lista obtida acima escolha um agravo de notificação para analisar. 

Em seguida, verifique quais são os anos disponíveis para o agravo de notificação escolhido. Para isso, execute o código abaixo:
```python
anos = SINAN.get_available_years('nome_do_agravo')
anos
```
## Extraindo os dados do SINAN
Agora que você já escolheu o agravo de notificação e o ano, vamos extrair os dados do SINAN. Para isso, execute o código abaixo:
```python
path = SINAN.download('nome_do_agravo', int(anos[3]))
df = pd.read_parquet(path)
```

## Analisando os dados
Agora que você já extraiu os dados do SINAN, vamos analisá-los. Para isso, vamos utilizar a biblioteca Pandas. Para começar, vamos importar a biblioteca Pandas e verificar o tamanho do DataFrame:
```python
import pandas as pd # Importando a biblioteca Pandas
df.shape # Verificando o tamanho do DataFrame
```
A biblioteca Pandas tem muitas funcionalidades, mas vamos utilizar apenas algumas delas. Para começar, vamos utilizá-la para salvar os dados baixados em um arquivo CSV. Para isso, execute o código abaixo:
```python
df.to_csv('nome_do_agravo.csv', index=False)
```
Isto permite que você não precise baixar os dados novamente toda vez que for analisá-los. Agora, vamos utilizar a biblioteca Pandas para ler os dados do arquivo CSV que acabamos de salvar. Para isso, execute o código abaixo:
```python
df = pd.read_csv('nome_do_agravo.csv')
```

## Tarefas de análise

### Análise exploratória dos dados
Agora que você já extraiu os dados do SINAN e os carregou em um DataFrame, vamos realizar uma análise exploratória dos dados. Para isso, utilize as funções da biblioteca Pandas para responder às seguintes perguntas, assumindo que o agravo escolhido foi a *dengue* (substitua pelo agravo escolhido):
1. Quantos casos de dengue foram notificados no Brasil em 2019?
2. Quantos casos de dengue foram notificados no Brasil em 2019, por município?
3. Quantos casos de dengue foram notificados no Brasil em 2019, por estado?
4. Quantos casos de dengue foram notificados no Brasil em 2019, por mês?
5. Quantos casos de dengue foram notificados no Brasil em 2019, por faixa etária?
6. Quantos casos de dengue foram notificados no Brasil em 2019, por sexo?
7. Quantos casos de dengue foram notificados no Brasil em 2019, por raça/cor?

Com os resultados obtidos, construa um relatório em LaTeX. O relatório deve conter as seguintes seções:
1. **Introdução:** Onde você deve explicar o que é o SINAN e o que é o agravo de notificação escolhido. Procure descobrir o código *CID10* (classificação internacional de doenças) para o agravo escolhido. Por exemplo, o código *CID10* para a dengue é **A90**.
2. **Metodologia:** Nesta seção, você deve explicar como os dados foram extraídos do SINAN e como foram analisados. Para isso, você deve explicar como a biblioteca PySUS foi utilizada para extrair os dados do SINAN e como a biblioteca Pandas foi utilizada para analisar os dados.
3. **Resultados:** Nesta seção, você deve apresentar os resultados obtidos na análise exploratória dos dados. Para isso, você deve apresentar os resultados obtidos nas perguntas 1 a 7 acima. Para cada pergunta, você deve apresentar os resultados em forma de tabela e gráfico. Para isso, utilize as funções da biblioteca Pandas para gerar as tabelas e gráficos.