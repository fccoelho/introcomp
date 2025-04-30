# Resposta ao exercícios da Lista 3

1. Usando o arquivo de dados Star_trek-Season_1.csv, descubra quantos episódios tem a temporada 1.
```bash
$ grep -c "Star Trek: The Original Series" Star_trek-Season_1.csv
```
2. Usando o arquivo de dados Star_trek-Season_1.csv, descubra quanto tempo durou a temporada 1.
Se você quiser contar o número de episódios, você pode usar o seguinte comando:
```bash
$ `$(wc -l Star_trek-Season_1.csv - 1)` # Subtrai 1 para não contar o cabeçalho
```

Se você quiser contar o tempo total em dias e semanas, você pode usar o seguinte script:
```bash
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
``` 

3. Usando o arquivo de dados Star_trek-Season_1.csv, descubra quantos episódios os alienígenas quase tomaram a Enterprise.
 Para resolver este exercício. primeiro, você precisa encontrar a coluna que contém esta informação. Esta coluna é a coluna 7. Esta coluna contém  apenas 0s e 1s, onde 0 significa que os alienígenas não tomaram a Enterprise e 1 significa que os alienígenas quase tomaram a Enterprise. Para contar quantos episódios os alienígenas quase tomaram a Enterprise, você pode usar o seguinte comando:

```bash
$ cut -d, -f 7 Star_Trek-Season_1.csv | grep -c "1"
```

4.Usando o arquivo de dados Star_trek-Season_1.csv, descubra em que episódios episódios o Dr. McCoy disse: "Damn it Jim!". retorne as datas de exibição destes episódios.

Para resolver este problema, você pode usar a mesma estratégia da questão anterior. Primeiro, você precisa encontrar a coluna que contém esta informação. Esta coluna é a coluna 15. Esta coluna contém  apenas 0s e 1s, onde 0 significa que o Dr. McCoy não disse "Damn it Jim!" e 1 significa que o Dr. McCoy disse "Damn it Jim!". Para contar quantos episódios o Dr. McCoy disse "Damn it Jim!", você pode usar o seguinte comando:
```bash
$ cut -d, -f 15 Star_Trek-Season_1.csv | grep -c "1"
```



