#!/bin/bash

for i in $(sort palavras_antigas.txt| uniq -i); do
    echo "$i $(grep -ic $i O_cortico.txt)" >> ocorrencias.txt
done
