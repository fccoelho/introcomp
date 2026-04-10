## ✅ Resolução dos Exercícios

### 1 a 21 (Exercícios Originais)

1. **Protocolo de comunicação**: Conjunto padronizado de regras que define como os dados são formatados, transmitidos, recebidos e interpretados entre dispositivos em uma rede.
2. **Principais protocolos**: `TCP`, `IP`, `UDP`, `HTTP/HTTPS`, `FTP`, `SSH`, `DNS`, `DHCP`, `ICMP`, `TLS/SSL`.
3. **Endereço IP**: Identificador lógico único atribuído a cada interface de rede que participa de uma comunicação baseada no protocolo IP.
4. **Quantidade de endereços**:
   - IPv4: $2^{32} \approx 4,29$ bilhões.
   - IPv6: $2^{128} \approx 3,4 \times 10^{38}$ (praticamente ilimitado).
5. **Endereço MAC**: Identificador físico de 48 bits gravado na placa de rede pelo fabricante. Único globalmente (teoricamente) e usado na camada de enlace.
6. **Servidor DNS**: Sistema que traduz nomes de domínio legíveis (ex: `exemplo.com`) em endereços IP numéricos, permitindo a localização de serviços na internet.
7. **Rede Local (LAN)**: Rede de computadores que abrange uma área geográfica restrita (residência, escritório, campus), geralmente usando Ethernet ou Wi-Fi.
8. **Roteador**: Dispositivo que encaminha pacotes entre redes distintas, atuando como gateway e decidindo o melhor caminho com base em tabelas de roteamento.
9. **Máscara `/24` (255.255.255.0)**: 
   - Define 256 endereços. O primeiro (`.0`) é o endereço de rede e o último (`.255`) é o de broadcast. Os 254 intermediários são para hosts.
   - Faixas privadas comuns (RFC 1918): `192.168.x.0/24`, `10.0.0.0/8`, `172.16.0.0/12`.
10. **CIDR (Classless Inter-Domain Routing)**: Notação que indica quantos bits são usados para a parte de rede (ex: `/24`). Em `/24`, há $2^{(32-24)} = 256$ endereços totais, sendo **254 úteis** para hosts.
11. **HTTP**: Transmite dados de hipermídia (HTML, JSON, XML, imagens, vídeos, etc.) em texto plano, sem criptografia.
12. **HTTPS**: HTTP Secure. Utiliza TLS/SSL para criptografar a comunicação, garantindo confidencialidade, integridade e autenticidade.
13. **Cópia via SSH**: Comando `scp` ou `rsync`. Ex: `scp documento.pdf usuario@192.168.1.50:/tmp/`
14. **Verificar acessibilidade**: Comando `ping`. Ex: `ping -c 4 8.8.8.8`
15. **Autenticação por chave SSH**: O cliente gera um par de chaves (pública/privada). A pública é copiada para `~/.ssh/authorized_keys` no servidor. O servidor desafia o cliente, que prova posse da chave privada sem enviá-la. Ex:
    ```bash
    ssh-keygen -t ed25519
    ssh-copy-id user@servidor
    ssh user@servidor  # conecta sem senha
    ```
16. **Porta SSH padrão**: `22/TCP`.
17. **Túnel SSH (Local Port Forwarding)**:
    ```bash
    ssh -L 8080:127.0.0.1:8080 usuario@servidor_remoto
    ```
    Após executar, acessar `http://localhost:8080` no navegador local encaminhará o tráfego criptografado até a porta `8080` do servidor.
18. **FTP anônimo**: Usuário `anonymous`. A senha geralmente é ignorada ou aceita qualquer valor (costuma-se usar um e-mail fictício).
19. **Listar FTP**: 
    - Via cliente interativo: `ftp> ls` ou `ftp> dir`
    - Via terminal: `curl -l ftp://ftp.exemplo.com --user anonymous:`
20. **Baixar arquivo FTP**: 
    - Interativo: `ftp> get arquivo.zip`
    - Terminal: `curl -O ftp://ftp.exemplo.com/arquivo.zip --user anonymous:`
21. **Baixar múltiplos `.zip`**: 
    - Interativo: `ftp> mget "*.zip"`
    - Terminal: `curl -O ftp://ftp.exemplo.com/*.zip --user anonymous:` (requer suporte do servidor)

---

### 22 a 30 (Exercícios Bash/Terminal)

22. **Verificar IPs das interfaces**:
    ```bash
    ip addr show
    # ou apenas: ip a
    ```

23. **Descobrir gateway padrão**:
    ```bash
    ip route show default
    # Saída típica: default via 192.168.1.1 dev eth0
    ```

24. **Conexões ativas e portas em escuta**:
    ```bash
    ss -tulpn
    # -t (TCP), -u (UDP), -l (listening), -p (processo), -n (numérico)
    ```

25. **Consultar registro MX**:
    ```bash
    dig gmail.com MX +short
    # ou: nslookup -type=MX gmail.com
    ```

26. **Cabeçalhos HTTP com curl**:
    ```bash
    curl -I http://example.com
    # -I faz requisição HEAD e exibe apenas cabeçalhos e código de status
    ```

27. **Rastrear rota (traceroute)**:
    ```bash
    traceroute 8.8.8.8
    # Alternativas: tracepath 8.8.8.8 ou mtr 8.8.8.8
    ```

28. **Testar porta com netcat**:
    ```bash
    nc -zv servidor.com 443
    # -z (scan only), -v (verbose). Saída: "succeeded!" ou "Connection refused/timeout"
    ```

29. **IP público via terminal**:
    ```bash
    curl -s ifconfig.me
    # ou: curl -s icanhazip.com ou curl -s api.ipify.org
    ```

30. **Script de ping automatizado**:
    ```bash
    #!/usr/bin/env bash
    hosts=("google.com" "github.com" "192.168.1.1")

    for host in "${hosts[@]}"; do
      if ping -c 1 -W 2 "$host" &>/dev/null; then
        echo "$host: ALIVE"
      else
        echo "$host: DOWN"
      fi
    done
    ```
    *Como usar*: Salve como `check_hosts.sh`, dê permissão com `chmod +x check_hosts.sh` e execute com `./check_hosts.sh`. O `-W 2` define timeout de 2 segundos por host.
