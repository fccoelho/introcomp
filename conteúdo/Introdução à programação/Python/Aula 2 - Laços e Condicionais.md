# Laços e Condicionais
Laços e Condicionais são estruturas de controle de fluxo, que permitem executar um bloco de código repetidamente até que uma condição seja atendida.
## Laços
### For
O laço for é usado quando sabemos o número de vezes que queremos executar um bloco de código.
```python
for i in range(5):
    print(i)
0
1
2
3
4
 ```
### While
O laço while é usado quando não sabemos o número de vezes que queremos executar um bloco de código.
```python
i = 0
while i < 5:
    print(i)
i = i + 1
0
1
2
3
4
 ```
### `break` e `continue`
O break é usado para interromper um laço.
```python
i = 0
while True:
    print(i)
    i = i + 1
    if i == 5:
        break
```
O `continue` é usado para pular para a próxima iteração do laço.


## Condicionais
### If
O if é usado para executar um bloco de código se uma condição for verdadeira.   
```python
if 5 > 2:
    print("5 é maior que 2")
5 é maior que 2
```
### Else
O else é usado para executar um bloco de código se uma condição for falsa.
```python
if 5 > 2:
    print("5 é maior que 2")
else:
    print("5 é menor que 2")
5 é maior que 2
```
### Elif
O elif é usado para executar um bloco de código se uma condição for falsa.
```python
if 5 > 2:
    print("5 é maior que 2")
elif 5 == 2:
    print("5 é igual a 2")
else:
    print("5 é menor que 2")
5 é maior que 2
```
## Operadores Lógicos
