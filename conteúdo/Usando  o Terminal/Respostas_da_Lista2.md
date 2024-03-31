# Respostas dos exercícios de programação shell (lista_2)
Estas respostas foram geradas pelo Co-pilot. Use com cuidado.

resposta do exercício 1:
```bash
echo "Shell Script é demais!"
```
resposta do exercício 2:
```bash
chmod +x nome_do_script.sh
```
resposta do exercício 3:
```bash
#!/bin/bash
echo "Shell Script é demais!"
```
resposta do exercício 4:
```bash
#!/bin/bash
echo $1
```
resposta do exercício 5:
```bash
#!/bin/bash
if [ -e $1 ]
then
  echo "O caminho $1 está habilitado!"
  if [ -w $1 ]
  then
    echo "Você tem permissão para editar $1"
  else
    echo "Você NÃO foi autorizado a editar $1"
  fi
else
  echo "O caminho $1 não existe"
fi
```
resposta do exercício 6:
```bash
#!/bin/bash
if grep "trybe" /etc/passwd
then
  echo "O usuário trybe está cadastrado no sistema"
else
  echo "Não existe um usuário chamado trybe"
fi
```
resposta do exercício 7:
```bash
ps -aux
```
resposta do exercício 8:
```bash
ps -aux | grep nome_do_processo
```
resposta do exercício 9:
```bash
ps -p 1
```
resposta do exercício 10:
```bash
less /var/log/syslog
```
resposta do exercício 11:
```bash
grep root /var/log/syslog
```
