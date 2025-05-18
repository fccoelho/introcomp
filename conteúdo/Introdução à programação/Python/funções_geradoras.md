# Funções geradoras
As funções geradoras são funções que retornam um iterável. Elas são definidas usando a palavra-chave `yield` ao invés de `return`.
As funções geradoras são ótimas para gerar dados de forma eficiente, pois não precisam ser armazenados na memória. 

Exemplo:
```python
def gerador():
    for i in range(10):
        yield i
```
A função geradora `gerador()` retorna um iterável, que pode ser iterado usando um loop `for`.

```python
for i in gerador():
    print(i)
```

Isso imprimirá os números de 0 a 9.

## Passando valores para as funções geradoras
As funções geradoras podem receber valores como argumentos. Isso é útil quando queremos passar valores para uma função geradora.

Exemplo:
```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value
```

Para usar a função geradora `accumulator()`, você precisa criar um objeto gerador usando a função `generator()`.
```python
# Uso da função geradora
acc = accumulator()
next(acc)  # Inicializa o gerador

print(acc.send(5))  # Envia 5, retorna 5
print(acc.send(10)) # Envia 10, retorna 15
print(acc.send(2))
```