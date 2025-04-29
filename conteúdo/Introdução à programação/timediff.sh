#!/bin/bash

egrep -o "[0-9]{4}-[0-9]{2}-[0-9]{2}" Star_Trek-Season_1.csv > datas # Retorna as datas do arquivo

date_i=$(head -n1 datas) # Pega a primeira data
date_f=$(tail -n1 datas) # Pega a última data

s1=$(date -d "$date_i" +%s)  # Converte date_i para segundos desde a época. A época é 1970-01-01 00:00:00 UTC
s2=$(date -d "$date_f" +%s)  # Converte date_f para segundos desde a época
diff_seconds=$((s2 - s1))
diff_days=$((diff_seconds / 86400))  # 86400 segundos em um dia

echo $diff_days dias
echo $((diff_days / 7)) semanas
