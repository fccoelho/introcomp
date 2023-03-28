#!/usr/bin/bash

x=10
y=20
export x
#echo $x $y

lista=(1 2 3 4 5 34 65)
frutas[0]=banana
frutas[1]=abacaxi
echo lista=${lista[@]}
echo $frutas # imprime primeiro elemento da array
echo ${frutas[1]} # imprime elemento 


# Arrays associativas
echo Testando Arrays associativas!
echo ===================
declare -A dicionario
dicionario["Brasil"]="Brasília"
dicionario["Goiás"]="Goiânia"
echo ${dicionario["Brasil"]}


## Laços
#x=0
#until $(($x<10));
#do
#echo $x
#x=$((x+1))
#done 
echo ======for======
for fruta in ${frutas[@]};
do
echo $fruta
done
