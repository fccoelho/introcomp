# Lista de exercícios de Python Nº 5

1. As regras para determinar se um ano é ou não um bissexto são as seguintes:
   - Qualquer ano divisível por 400 é um ano bissexto.
   - Dos anos restantes, qualquer ano divisível por 100 não é um ano bissexto.
   -  Dos anos restantes, qualquer ano divisível por 4 é um ano bissexto.
   -  Todos os outros anos não são anos bissextos.
   
    **Tarefa:**
    Criar uma função em Python chamada bissexto que receba como parâmetro de entrada um número de um ano
    e retorne como parâmetro de saída True se ele é bissexto e False caso contrário.

2. Uma boa senha é definida segundo os seguintes critérios:
   -  possui pelo menos 8 caracteres
   - contém pelo menos uma letra maiúscula
   - contém pelo menos uma letra minúscula
   - contém pelo menos um número
   
   **Tarefa:**
   Criar uma função em Python chamada boaSenha que receba como parâmetro de entrada uma string retorne
   como parâmetro de saída True se é uma boa senha e False caso contrário.
3. Uma data mágica é uma data em que o dia multiplicado pelo mês é igual ao ano de dois dígitos. Por exemplo, 10
de junho de 1960 é uma data mágica porque junho é o sexto mês e 6 vezes 10 é 60, que é igual ao ano de dois
dígitos.

    **Tarefa:**
Criar uma função em Python chamada dataMagica que receba como parâmetro de entrada uma data (pode ser
uma string no formato ddmmaaaa, ou no formato dd/mm/aaaa) retorne como parâmetro de saída True se é uma
data mágica e False caso contrário.
4. Um número perfeito é um número inteiro positivo que é igual à soma de seus divisores próprios positivos. Por exemplo, 6 é um número perfeito porque seus divisores próprios positivos são 1, 2 e 3, e 1 + 2 + 3 = 6.

    **Tarefa:** Criar uma função em Python chamada numeroPerfeito que receba como parâmetro de entrada um número inteiro positivo e retorne como parâmetro de saída True se é um número perfeito e False caso contrário.
5. Considere a seguinte série:
$$S_k = \sum_{n=0}^k \frac{(-1)^n}{2n-1} = \frac{1}{1}- \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} \ldots$$
**Tarefa:** Criar uma função em Python chamada serie que receba como parâmetro de entrada um inteiro k e retorne como parâmetro de saída o valor da série S_k.