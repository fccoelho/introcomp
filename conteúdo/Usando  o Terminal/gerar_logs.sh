#!/bin/bash

# Arrays com dados variados
IPS=("192.168.1.10" "192.168.1.15" "192.168.1.55" "192.168.1.100" "192.168.1.101"
     "10.0.0.5" "10.0.0.8" "10.0.0.15" "10.0.0.20" "10.0.0.25"
     "172.16.0.20" "172.16.0.25" "172.16.0.30" "172.16.0.35" "172.16.0.40"
     "203.0.113.50" "203.0.113.51" "203.0.113.52" "198.51.100.10" "198.51.100.11")

URLS=("/index.html" "/home" "/about" "/contact" "/products" "/services"
      "/login" "/logout" "/register" "/dashboard" "/profile" "/settings"
      "/api/users" "/api/products" "/api/orders" "/api/auth" "/api/data"
      "/admin/config" "/admin/users" "/admin/logs" "/admin/settings"
      "/style.css" "/script.js" "/img/logo.png" "/img/banner.jpg" "/favicon.ico"
      "/search?q=test" "/search?q=product" "/search?q=SELECT * FROM users"
      "/api/users?id=1" "/api/users?id=5" "/api/item/1" "/api/item/10"
      "/docs/readme.pdf" "/download/file.zip" "/upload" "/backup")

METODOS=("GET" "GET" "GET" "GET" "POST" "POST" "PUT" "DELETE")

STATUS_CODES=("200" "200" "200" "200" "200" "201" "204" "301" "302"
              "400" "401" "403" "404" "404" "500" "502" "503")

USER_AGENTS=("Mozilla/5.0" "Mozilla/5.0" "Mozilla/5.0" "Mozilla/5.0"
             "curl/7.68.0" "curl/7.68.0" "Python-requests" "wget/1.21"
             "sqlmap/1.0" "PostmanRuntime/7.29" "axios/0.21.1")

# Gerar 488 linhas adicionais (total de 500)
for i in $(seq 1 488); do
    # Selecionar elementos aleatórios
    IP=${IPS[$RANDOM % ${#IPS[@]}]}
    URL=${URLS[$RANDOM % ${#URLS[@]}]}
    METODO=${METODOS[$RANDOM % ${#METODOS[@]}]}
    STATUS=${STATUS_CODES[$RANDOM % ${#STATUS_CODES[@]}]}
    AGENT=${USER_AGENTS[$RANDOM % ${#USER_AGENTS[@]}]}

    # Gerar timestamp variado (10/Oct/2023)
    HOUR=$((8 + RANDOM % 14))  # Entre 08:00 e 22:00
    MINUTE=$((RANDOM % 60))
    SECOND=$((RANDOM % 60))

    # Formatar minutos e segundos com zero à esquerda se necessário
    MINUTE_FMT=$(printf "%02d" $MINUTE)
    SECOND_FMT=$(printf "%02d" $SECOND)

    # Gerar tamanho da resposta baseado no status
    case $STATUS in
        200|201) SIZE=$((1000 + RANDOM % 5000));;
        301|302) SIZE=$((200 + RANDOM % 300));;
        400|401|403|404) SIZE=$((100 + RANDOM % 500));;
        500|502|503) SIZE=$((200 + RANDOM % 400));;
        204) SIZE=0;;
        *) SIZE=$((500 + RANDOM % 2000));;
    esac

    # Escrever linha no formato Apache Combined Log
    echo "$IP - - [10/Oct/2023:${HOUR}:${MINUTE_FMT}:${SECOND_FMT} +0000] \"${METODO} ${URL} HTTP/1.1\" ${STATUS} ${SIZE} \"-\" \"${AGENT}\"" >> access.log
done

echo "Arquivo access.log gerado com sucesso!"
echo "Total de linhas: $(wc -l < access.log)"
