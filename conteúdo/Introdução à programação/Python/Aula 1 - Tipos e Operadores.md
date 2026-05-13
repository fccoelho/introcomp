# Tipos e Operadores no Python
Python é uma linguagem de tipagem dinâmica, ou seja, o tipo de dado de uma variável é definido no momento em que o valor é atribuído a ela.

## Tipos de Dados
- int: números inteiros
- float: números reais
- str: strings
- bool: booleanos
- list: listas
- tuple: tuplas
- dict: dicionários
- set: conjuntos
- NoneType: tipo especial para representar o valor nulo
- object: tipo base para todos os outros tipos
- complex: números complexos
- range: intervalos
- slice: fatias
- memoryview: visualização de memória
- bytearray: array de bytes
- bytes: bytes
- frozenset: conjuntos imutáveis
- type: tipo

### Exemplos de usos dos tipos
```python
x = 10
print(type(x))
<class 'int'>
x = 10.5
print(type(x))
<class 'float'>
```
## Operadores
- Aritméticos: +, -, *, /, %, **, //
- Relacionais: ==, !=, >, <, >=, <=
- Lógicos: and, or, not
- Bitwise: &, |, ^, ~, <<, >>
- Identidade: is, is not
- Atribuição: =, +=, -=, *=, /=, %=, **=, //=
- Precedência: ()
### Examplos de usos dos operadores
#### Operações aritméticas in-place
 ```python
x = 10 
x += 5
print(x)
15
x *= 2
print(x)
30
x /= 3
print(x)
```
#### Operadores relacionais
```python
x = 10
print(x == 10)
True
print(x != 10)
False
print(x > 10)
False
print(x < 10)
 False
print(x >= 10)
True
```
#### Operadores lógicos: and, or,  not
```python
x = True   
print(x and False)
 False
print(x or False)
 True
print(not x)
 False
```
Existe um uso comum de operadores and e or chamado truque de and/or:
```python
x = 0 or 10
print(x)
10
x = 0 and 10
print(x)
0
```
#### Operadores bitwise

```python
x = 10
print(x & 5)
0
print(x | 5)
15
print(x ^ 5)
15
```
Para entender essas operações, vamos primeiro converter os números para **base 2 (binário)** e alinhá-los por posição de bit. No Python, os inteiros são representados internamente em binário, e as operações `&`, `|` e `^` atuam **bit a bit**.

**Representação binária**
```
  8  4  2  1   ← pesos de cada posição (2³, 2², 2¹, 2⁰)
  1  0  1  0   ← 10 = 8 + 2
  0  1  0  1   ←  5 = 4 + 1
```
*(Usamos 4 bits apenas para fins didáticos; o Python trabalha com o tamanho necessário.)*

Agora, aplicamos cada operação coluna por coluna:

---

1. `&` (AND bit a bit)
Retorna `1` **apenas se ambos os bits forem `1`**. Caso contrário, retorna `0`.
```
  1 & 0 = 0
  0 & 1 = 0
  1 & 0 = 0
  0 & 1 = 0
  ─────
  0 0 0 0  → 0₁₀
```
✅ `print(x & 5)` → `0`

---

2. `|` (OR bit a bit)
Retorna `1` **se pelo menos um dos bits for `1`**. Só retorna `0` se ambos forem `0`.
```
  1 | 0 = 1
  0 | 1 = 1
  1 | 0 = 1
  0 | 1 = 1
  ─────
  1 1 1 1  → 8+4+2+1 = 15₁₀
```
✅ `print(x | 5)` → `15`

---

3. `^` (XOR bit a bit)
Retorna `1` **se os bits forem diferentes**, e `0` se forem iguais.
```
  1 ^ 0 = 1  (diferentes)
  0 ^ 1 = 1  (diferentes)
  1 ^ 0 = 1  (diferentes)
  0 ^ 1 = 1  (diferentes)
  ─────
  1 1 1 1  → 15₁₀
```
✅ `print(x ^ 5)` → `15`

---

💡 *Por que `|` e `^` deram o mesmo resultado?*

Observe que **não há nenhuma coluna onde ambos os números têm `1` ao mesmo tempo**. Quando não há sobreposição de bits `1`, as operações OR e XOR são matematicamente equivalentes. 

Se você testar com números que compartilham bits `1` (ex: `10 & 6` ou `10 | 6`), verá que `|` e `^` passam a produzir resultados diferentes.

📊 **Tabela resumo das regras bit a bit**

| Bit A | Bit B | `A & B` | `A \| B` | `A ^ B` |
|:-----:|:-----:|:-------:|:--------:|:-------:|
|   0   |   0   |    0    |    0     |    0    |
|   0   |   1   |    0    |    1     |    1    |
|   1   |   0   |    0    |    1     |    1    |
|   1   |   1   |    1    |    1     |    0    |



