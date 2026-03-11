# Guia de Aula: Bases Numéricas na Computação para Ciência de Dados


---

## 1. Introdução: Por que estudamos bases numéricas?

As bases numéricas são sistemas de numeração que utilizam símbolos para representar quantidades. A base numérica mais comum no dia-a-dia das pessoas é a **Base 10 (Decimal)**, que utiliza os algarismos de 0 a 9. Provavelmente usamos essa base porque temos 10 dedos nas mãos.

No entanto, na computação e na Ciência de Dados, lidamos constantemente com outras bases:
*   **Base 2 (Binária):** A linguagem nativa do hardware.
*   **Base 8 (Octal):** Historicamente importante, ainda usada em permissões de arquivos Linux.
*   **Base 16 (Hexadecimal):** Usada para representar memória, cores e hashes de forma compacta.

**Por que isso importa para um Cientista de Dados?**
1.  **Memória e Performance:** Entender como os dados são armazenados (bits e bytes) ajuda a escolher tipos de variáveis eficientes (ex: `int8` vs `int64` em Pandas/NumPy), economizando RAM em grandes datasets.
2.  **Manipulação de Bits:** Operações bitwise são usadas em criptografia, compressão de dados e filtragem de flags.
3.  **Depuração:** Endereços de memória e erros de sistema frequentemente aparecem em hexadecimal.
4.  **Imagens:** Cores em processamento de imagem são definidas em hexadecimal (RGB).

---

## 2. Base 2 (Binária)

A base 2 é a base utilizada pelos computadores para representar informações internamente. Os computadores são máquinas digitais que trabalham com dois estados físicos (tensão alta/baixa, magnético/não magnético), representados por **0** e **1**.

*   **Bit:** A menor unidade de informação (um 0 ou um 1).
*   **Byte:** Um conjunto de 8 bits.

### Como ler um número binário
Assim como na base 10 cada posição representa uma potência de 10 ($10^0, 10^1, 10^2...$), na base 2 cada posição representa uma potência de 2 ($2^0, 2^1, 2^2...$), lendo da direita para a esquerda.

**Exemplo:** O número `1011` na base 2.

| Posição | 3 | 2 | 1 | 0 |
| :--- | :---: | :---: | :---: | :---: |
| **Bit** | **1** | **0** | **1** | **1** |
| **Cálculo** | $1 \times 2^3$ | $0 \times 2^2$ | $1 \times 2^1$ | $1 \times 2^0$ |
| **Valor** | 8 | 0 | 2 | 1 |

**Total:** $8 + 0 + 2 + 1 = \mathbf{11}$ (na base 10).

---

## 3. Base 8 (Octal)

A base 8 utiliza os algarismos de **0 a 7**.
*   **Relação com Binário:** Cada dígito octal representa exatamente **3 bits**.
*   **Uso Prático:** Muito comum em sistemas Unix/Linux para definir permissões de arquivos (leitura, escrita, execução).

### Conversão Binário $\leftrightarrow$ Octal
Para converter, agrupamos os bits de 3 em 3 (da direita para a esquerda).

**Exemplo:** Converter `1011` (binário) para Octal.
1.  Complete com zeros à esquerda para formar grupos de 3: `001 011`.
2.  Converta cada grupo:
    *   `001` = $1$
    *   `011` = $3$ ($2+1$)
3.  Resultado: **13** (na base 8).

> *Nota:* O valor numérico é o mesmo (11 em decimal), mas a representação octal agrupa os bits de forma diferente da hexadecimal.

---

## 4. Base 16 (Hexadecimal)

A base 16 utiliza os algarismos **0-9** e as letras **A-F** para representar os valores de 10 a 15.
*   **Relação com Binário:** Cada dígito hexadecimal representa exatamente **4 bits** (um *nibble*).
*   **Uso Prático:** Endereços de memória (RAM), códigos de cor (HTML/CSS), hashes (MD5, SHA), MAC Addresses.

| Decimal | Hex | Binário (4 bits) |
| :---: | :---: | :---: |
| 10 | A | 1010 |
| 11 | B | 1011 |
| 12 | C | 1100 |
| 13 | D | 1101 |
| 14 | E | 1110 |
| 15 | F | 1111 |

### Conversão Binário $\leftrightarrow$ Hexadecimal
Agrupamos os bits de 4 em 4.

**Exemplo:** Converter `1011` (binário) para Hexadecimal.
1.  O grupo é `1011`.
2.  Valor decimal do grupo: $8+0+2+1 = 11$.
3.  Em Hex, 11 é representado pela letra **B**.
4.  Resultado: **0xB** (o prefixo `0x` indica hexadecimal em programação).


---

## Aplicação Prática: Permissões de Arquivo no Linux (Base 8)

Um dos usos mais comuns da base octal na computação moderna é o gerenciamento de permissões de arquivos em sistemas Unix/Linux. Para um Cientista de Dados, isso é crucial ao criar *scripts* de automação ou configurar ambientes de servidor.

### Estrutura das Permissões
As permissões são divididas em três categorias de usuários:
1.  **Dono (User):** Quem criou o arquivo.
2.  **Grupo (Group):** Usuários que pertencem ao mesmo grupo do arquivo.
3.  **Outros (Others):** Qualquer outro usuário no sistema.

Para cada categoria, existem três tipos de permissões possíveis, que mapeiam diretamente para **3 bits** (base 2):

| Permissão | Símbolo | Valor Octal | Valor Binário |
| :--- | :---: | :---: | :---: |
| **Leitura** (Read) | `r` | **4** | `100` |
| **Escrita** (Write) | `w` | **2** | `010` |
| **Execução** (Execute) | `x` | **1** | `001` |
| **Nenhuma** | `-` | **0** | `000` |

### Como Calcular o Código Octal
Para definir a permissão, somamos os valores das permissões desejadas para cada categoria.

**Exemplo Prático:** Vamos configurar um script de análise de dados chamado `etl_pipeline.sh` com a permissão **755**.

1.  **Primeiro Dígito (Dono): 7**
    *   Cálculo: $4 (\text{leitura}) + 2 (\text{escrita}) + 1 (\text{execução}) = 7$
    *   Binário: `111`
    *   Significado: O dono pode ler, editar e **executar** o script.

2.  **Segundo Dígito (Grupo): 5**
    *   Cálculo: $4 (\text{leitura}) + 0 (\text{sem escrita}) + 1 (\text{execução}) = 5$
    *   Binário: `101`
    *   Significado: O grupo pode ler e **executar**, mas não pode modificar o script.

3.  **Terceiro Dígito (Outros): 5**
    *   Cálculo: $4 (\text{leitura}) + 0 (\text{sem escrita}) + 1 (\text{execução}) = 5$
    *   Binário: `101`
    *   Significado: Qualquer usuário pode ler e **executar**.

**Comando no Terminal:**
```bash
chmod 755 etl_pipeline.sh
```

**Verificando no Terminal:**
Ao listar os arquivos com detalhes (`ls -l`), você verá a representação simbólica correspondente ao octal:

```bash
ls -l etl_pipeline.sh
# Saída esperada: -rwxr-xr-x 1 usuario grupo ... etl_pipeline.sh
```
*   `rwx` (Dono) = 7
*   `r-x` (Grupo) = 5
*   `r-x` (Outros) = 5

> **Dica para Ciência de Dados:** Se você criar um arquivo de dados sensíveis (ex: `clientes.csv`), geralmente quer que apenas o dono leia e escreva. O código octal ideal seria **600** ($4+2=6$ para o dono, $0$ para os outros).

---

## 5. Laboratório Prático: Terminal Bash

O terminal Linux/Unix (Bash) possui ferramentas nativas poderosas para manipular bases numéricas. Abra seu terminal e tente os seguintes exercícios.

### Exercício 1: Conversão Básica com Bash
O Bash permite especificar a base de entrada usando o formato `base#numero`.

1.  **Binário para Decimal:**
    Digite o comando abaixo para converter `1011` (binário) para decimal.
    ```bash
    echo $((2#1011))
    ```
    *Saída esperada:* `11`

2.  **Octal para Decimal:**
    Converta `13` (octal) para decimal.
    ```bash
    echo $((8#13))
    ```
    *Saída esperada:* `11`

3.  **Hexadecimal para Decimal:**
    Converta `B` (hex) para decimal.
    ```bash
    echo $((16#B))
    ```
    *Saída esperada:* `11`

### Exercício 2: Formatando Saídas (Decimal para outras bases)
Use o comando `printf` para converter um número decimal para outras representações.

1.  **Decimal para Hexadecimal:**
    ```bash
    printf "%x\n" 11
    ```
    *Saída esperada:* `b` (letras minúsculas por padrão)

2.  **Decimal para Hexadecimal (Maiúsculas):**
    ```bash
    printf "%X\n" 11
    ```
    *Saída esperada:* `B`

3.  **Decimal para Octal:**
    ```bash
    printf "%o\n" 11
    ```
    *Saída esperada:* `13`

### Exercício 3: Permissões de Arquivo (Contexto Octal)
Em Linux, as permissões de arquivos são armazenadas em octal.
1.  Crie um arquivo dummy:
    ```bash
    touch dados.csv
    ```
2.  Veja as permissões atuais (o número no início ou use `stat`):
    ```bash
    stat -c "%a %n" dados.csv
    ```
    *Explicação:* O número `644` ou `664` é octal.
    *   `6` (Leitura + Escrita) = Binário `110`
    *   `4` (Apenas Leitura) = Binário `100`
3.  Mude a permissão para permitir execução (adicione `1` ao último dígito):
    ```bash
    chmod 645 dados.csv
    stat -c "%a %n" dados.csv
    ```
    *Pergunta:* O que o último bit `1` representa em binário no contexto de permissões? (Resposta: Execução).

### Exercício 4: Operações Bitwise (E, OU, XOR)
Cientistas de dados usam máscaras de bits para filtrar dados. No Bash, usamos `&` (AND), `|` (OR), `^` (XOR).

1.  **Operação AND (`&`):**
    ```bash
    echo $(( 5 & 3 ))
    ```
    *Lógica:*
    `5` = `101`
    `3` = `011`
    `&` = `001` (Resultado decimal: 1)

2.  **Operação OR (`|`):**
    ```bash
    echo $(( 5 | 3 ))
    ```
    *Lógica:*
    `5` = `101`
    `3` = `011`
    `|` = `111` (Resultado decimal: 7)

3.  **Desafio de Máscara:**
    Imagine que você tem um número de status `12` (`1100` em binário). Você quer verificar se o bit da posição 3 (valor 8) está ligado.
    ```bash
    echo $(( 12 & 8 ))
    ```
    *Se o resultado for maior que 0, o bit está ligado.*

---

## 6. Exercícios de Fixação (Papel e Caneta)

1.  **Conversão Decimal -> Binário:**
    Converta o número decimal **25** para binário. (Dica: Divida sucessivamente por 2 e anote os restos).
2.  **Conversão Binário -> Hex:**
    Converta o binário `11110000` para Hexadecimal. (Dica: Quebre em dois grupos de 4 bits).
3.  **Memória:**
    Se um sensor de IoT envia dados em um inteiro de 8 bits (1 byte) sem sinal (unsigned), qual é o valor máximo decimal que ele pode representar?
    *   a) 100
    *   b) 255
    *   c) 256
    *   d) 128
4.  **Cores:**
    A cor branca em HTML é representada por `#FFFFFF`. Quantos bits são necessários para representar essa cor? (Dica: Cada caractere Hex são 4 bits).

---

## 7. Gabarito Comentado

1.  **25 em Binário:** `11001` ($16 + 8 + 0 + 0 + 1$).
2.  **11110000 em Hex:** `F0` (`1111` = F, `0000` = 0).
3.  **Máximo 8 bits:** **b) 255**. ($2^8 - 1 = 256 - 1$). O zero conta como um estado.
4.  **Bits na cor branca:** `FFFFFF` tem 6 dígitos hex. $6 \times 4 \text{ bits} = 24 \text{ bits}$.

---

## 8. Dica para Python (Ciência de Dados)

Como você provavelmente usará Python, saiba que ele lida nativamente com essas bases:

```python
# Binário
bin(11)       # Retorna '0b1011'
int('1011', 2) # Retorna 11

# Hexadecimal
hex(11)       # Retorna '0xb'
int('B', 16)   # Retorna 11

# Octal
oct(11)       # Retorna '0o13'
```



