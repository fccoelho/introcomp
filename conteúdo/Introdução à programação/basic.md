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

1. Crie um programa simples para imprimir “Alô, Fulano!”
```basic
input "qual o seu nome? " N$
print "Olá ", N$, "!"
```

Fácil, não? Agora desafie-se com os demais exercícios! Complete o programas abaixo:
## Desafio
1. Crie um programa que imprima a sequência de Fibonacci até o décimo termo. 


```basic
a=0
b=1
```
2. Crie um programa que imprima a tabuada de 7.
3. Crie um programa que solicite dois números ao usuário e imprima a média deles.
4. considere o programa abaixo:
```basic
print "Aperte uma tecla para continuar"
print "(O program irá continuar após 10 segundos)"
clear screen
for a=1 to 10
  print a
  k$ = inkey$(1)
  if (k$<>"") then goto done
  endif
next a
label done
print "Você pressionou a tecla ", k$
``` 
Agora escreva um programa similar, que faça uma pergunta do tipo "sim(S) ou não(N)"e caso o usuário não responda em 10 segundos, ou responda "N", saia do programa. caso contrario, imprima a resposta do usuário. Utilize o comando `goto` ou `gosub` para implementar a lógica.

5. Considere o programa abaixo:
```basic
open window 200,200
line 50,50, 100,100
```
Agora escreva um programa que desenhe um quadrado de lado 50, e um triângulo equilátero de lado 50. Utilize o comando `line` para desenhar os triângulos. Dica: a altura de um triângulo equilátero de lado `L` é `L*sqrt(3)/2`.


