# Lista de Exercícios 2
## Exercícios de programação shell Bash
1. Crie um script que imprime as palavras "Shell Script é demais!" na tela.
2. Torne o script do exercício anterior executável com o comando `chmod +x`. Se você não se lembra como fazer isso, revise a aula sobre permissões.
3. Adicione a linha **she-bang** ao seu script.
2. Modifique o script do exercício anterior de forma que ele aceite um argumento.
3. Escreva um script que verifique se o caminho até um arquivo existe (`$1`). Se ele existir, imprima na tela: "O caminho `caminho_do_arquivo` está habilitado!". Então, verifique se você tem permissão de escrita no arquivo. Se tiver, mostre a mensagem: "Você tem permissão para editar `caminho_do_arquivo`". Caso contrário, mostre a mensagem: "Você NÃO foi autorizado a editar `caminho_do_arquivo`".
4. Escreva um script que, baseado no arquivo `/etc/passwd`, verifique se existe um usuário chamado `trybe`. Se não existir, imprima na tela: "Não existe um usuário chamado trybe". Caso contrário, imprima na tela: "O usuário trybe está cadastrado no sistema".

### Usando pipes
1. Liste os processos do sistema usando o comando `ps -aux`.
2. Liste os processos do sistema usando o comando `ps -aux` e use um segundo comando para buscar por um processo específico.
3. Liste informações sobre o processo cujo PID é 1.
4. Abra o LOG do sistema (/var/log/syslog) no paginador `less`. Use a tecla `/` para buscar por `cron`, que é o nome de um serviço agendador de tarefas no Linux.
5. Busque por `root` no arquivo `/var/log/syslog`, sem usar o less.
6. Liste os arquivos de log da pasta `/var/log` que foram modificados nas últimas 24 horas.
7. Liste todos os arquivos de log da pasta `/var/log` que não são arquivos de texto.
8. Liste todos os arquivos de log da pasta `/var/log` que são arquivos de texto e que, contendo a palavra `log`, não contêm a palavra `system`.
9. Extraia a data e hora da última vez que o sistema foi reiniciado do arquivo `/var/log/syslog`.
10. Liste o conteúdo de `/etc/passwd` e conte o número de linhas que não contêm a palavra `false`.

### usando o editor `sed`
1. Utilizando o editor `sed`, crie um arquivo de texto chamado `frutas.txt` com as seguintes palavras:
```
Banana
Maçã
Pera
Uva
```
2. Utilizando o editor `sed`, adicione a palavra `Melão` no arquivo `frutas.txt` após a palavra `Banana`.
3. Utilizando o editor `sed`, adicione a palavra `Laranja` no arquivo `frutas.txt` após a palavra `Pera`.
4. Utilizando o editor `sed`, remova a palavra `Pera` do arquivo `frutas.txt`.
5. Usando o editor `sed`, combinado com o `grep`, liste apenas as frutas que contêm a letra `e`.
6. Use o editor `sed` em um pipeline com comando cut para substituir a palavra `Uva` por `Morango` e, em seguida, corte a primeira letra da primeira linha do arquivo `frutas.txt`.


