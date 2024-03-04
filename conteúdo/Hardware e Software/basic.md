# Introdução ao Basic com Yabasic

O objetivo desta aula é ter uma noção básica de como era a interface básica com o usuário nos primeiros computadores pessoais: Um simples interpretador basic.

O Basic foi a linguagem escolhida para estes computadores por sua simplicidade. Hoje em dia é cada vez menos utilizada, escontrando utilização ainda como linguagem ara scriptação de alguns aplicativos que tiveram origem na época em que o Basic ainda era uma linguagem popular.

Vamos começar com um exercício de leitura de código. Tente entender qual resultado do código abaixo:

```basic
clear screen
print "Press 'q' to quit ..."
label again
print color("green") "Hello ";
print color("blue") "World !   ";
if (inkey$(1)="q") exit
goto again
```

Conseguiu? teste sua intepretação executando este código no interpretador [yabasic](https://2484.de/yabasic/).

O Yabasic é uma implementação moderna de uma linguagem antiga cujo interesse, atualmente é meramente histórica, mas nos ensina a entender a evolução das linguagens.
# Exercícios
[Esta lista](/conteúdo/Introdução%20à%20programação%20em%20Python/lista1.md) conté vários exercícios simples de programação, que podem ser resolvidos em qualquer linguagem. vamos resolver o primeiro em basic!

1. Crie um programa simples para imprimir “Hello, world!”
```basic
print "Hello, world"
```

Fácil, não? Agora desafie-se com os demais exercícios! Complete o programas abaixo:
## Desafio
1. Crie um programa que imprima a sequência de Fibonacci até o décimo termo. 


```basic
a=0
b=1
```
2. Crie um programa que imprima a tabuada de 7.

3. Calcule a soma de dois números e imprima o resultado.
4. Calcule a média de 5 números e imprima o resultado.
5. Crie um programa que receba um número e imprima se ele é par ou ímpar.
6. Crie um programa que receba um número e imprima se ele é primo ou não.
7. Crie um programa que receba um número e imprima a tabuada desse número.
8. Crie um programa que receba um número e imprima a tabuada de todos os números de 1 até esse número.
9. Crie um programa que receba um número e imprima a tabuada de todos os números ímpares de 1 até esse número.
10. Crie um programa que receba um número e imprima a tabuada de todos os números pares de 1 até esse número.

