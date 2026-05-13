# Funções Builtin do Python
O Python possui uma biblioteca de funções builtin, ou seja, funções que já existem no Python. Para listar estas funções, podemos usar a função `dir()`.

## A função `len`
A função `len` retorna o tamanho de um objeto.
```python
print(len('Olá mundo!'))
print(len([1, 2, 3, 4, 5]))
```
## A função `zip`
A função `zip` junta dois ou mais objetos iteráveis.
```python
for nome, idade in zip(['João', 'Maria', 'Pedro'], [18, 16, 14]):
    print(f'{nome} tem {idade} anos')
```
## A função `map`
A função `map` aplica uma função a cada elemento de um objeto iterável.  O resultado é um objeto iterável.
```python
def quadrado(n):
    return n ** 2

print(list(map(quadrado, [1, 2, 3, 4, 5])))
```
