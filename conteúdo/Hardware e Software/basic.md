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
