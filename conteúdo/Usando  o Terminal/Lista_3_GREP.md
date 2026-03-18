Esta lista foca em **análise de logs real**, **expressões regulares complexas** (incluindo *lookarounds* e *backreferences* com `grep -P`), **pipelines robustos** (combinando `grep`, `awk`, `sed`, `sort`, `uniq`, `cut`) e **cenários de segurança/auditoria**.

---

### 🚀 Parte 2: 20 Exercícios Avançados de GREP + Pipelines

**Análise de Segurança e Logs**
1.  **Top IPs Erros:** Extraia apenas os endereços IP que receberam códigos de status HTTP **4xx ou 5xx** no `access.log`, conte a ocorrência de cada IP e mostre os 3 maiores ofensores.
2.  **Brute Force SSH:** Identifique IPs no `auth.log` que tiveram **mais de 2** tentativas de senha falhadas (`Failed password`).
3.  **SQL Injection:** Encontre linhas no `access.log` que contenham padrões suspeitos de SQL Injection (palavras como `SELECT`, `UNION`, `DROP` na URL), ignorando maiúsculas/minúsculas.
4.  **Acesso Root:** Liste todas as linhas do `auth.log` onde houve sucesso (`Accepted`) **OU** falha (`Failed`) envolvendo o usuário `root`.
5.  **Comandos Proibidos:** No `auth.log`, encontre tentativas de `sudo` que foram negadas (`command not allowed`) e extraia apenas o comando que o usuário tentou executar.
6.  **Correlação de IPs:** Extraia uma lista única de IPs que aparecem **tanto** no `access.log` quanto no `auth.log` (interseção de conjuntos).
7.  **Horário de pico:** Extraia a hora (HH) de todas as requisições no `access.log` e conte quantas requisições ocorreram em cada hora.
8.  **User Agents Suspeitos:** Encontre linhas no `access.log` onde o User Agent **não** seja "Mozilla/5.0" (ex: curl, python, sqlmap).
9.  **Extração de Credenciais (Auditoria):** No `config.ini`, encontre linhas que contenham chaves sensíveis (`password`, `api_key`, `secret`) e mostre apenas o **valor** após o `=`, removendo espaços.
10. **Validação de Email:** Extraia do `config.ini` apenas endereços de email válidos (deve conter @ e domínio com pelo menos 2 letras).

**Expressões Regulares Complexas (Regex)**
11. **Palavras Duplicadas:** Encontre linhas em qualquer arquivo que contenham uma palavra repetida consecutivamente (ex: "erro erro"), usando *backreferences*.
12. **Lookaround (Perl Regex):** No `access.log`, extraia apenas o código de status HTTP (ex: 200, 404) usando *lookbehind* e *lookahead* (não capture as aspas ou espaços ao redor).
13. **IPv4 Estrito:** Crie um regex que valide estritamente um IPv4 (0-255 em cada octeto) e filtre linhas do `access.log` que contenham IPs inválidos (se houver) ou apenas valide os existentes.
14. **Conteúdo entre Delimitadores:** Extraia todo o texto que está entre aspas duplas `"` na coluna da requisição do `access.log` (ex: `"GET /index.html HTTP/1.1"`).
15. **Versão Semântica:** Se houvesse versões (ex: v1.2.3) no texto, crie um regex para capturar padrões de versão semântica (X.Y.Z). (Simule adicionando uma linha ou use o existente).
16. **Linhas Vazias ou Comentários:** No `config.ini`, conte quantas linhas são comentários (começam com `#`) ou estão vazias, usando uma única expressão regular.
17. **Negativa Complexa:** Encontre linhas no `access.log` que contenham "GET" mas **não** contenham "200" e **não** contenham "css" ou "png" (filtros múltiplos).
18. **Extração de Portas:** No `auth.log`, extraia apenas o número da porta SSH (ex: `port 22`) usando `grep -oP`.
19. **Formato de Data:** Extraia as datas no formato `DD/Mon/YYYY` do `access.log` e converta o separador `/` para `-` usando `sed` após o `grep`.
20. **Relatório de Auditoria:** Crie um único comando pipeline que gere um resumo: "Total de Requests: X, Total de Erros 5xx: Y, IPs Únicos: Z".

---

### ✅ Parte 3: Soluções Detalhadas

**1. Top IPs Erros (4xx/5xx)**
```bash
grep -E "\" [45][0-9]{2} " access.log | grep -oE "^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" | sort | uniq -c | sort -rn | head -3
```
*Explicação:* Filtra status 4xx/5xx -> Extrai IP no início da linha -> Conta ocorrências -> Ordena numericamente invertido -> Mostra top 3.

**2. Brute Force SSH (>2 falhas)**
```bash
grep "Failed password" auth.log | grep -oE "from [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" | cut -d' ' -f2 | sort | uniq -c | awk '$1 > 2'
```
*Explicação:* Filtra falhas -> Extrai IP após "from" -> Corta o espaço -> Conta -> Filtra quem tem mais de 2.

**3. SQL Injection**
```bash
grep -iE "(SELECT|UNION|DROP|INSERT)" access.log
```
*Explicação:* `-i` ignora case, `-E` permite OR (`|`). Busca palavras chave comuns de SQL injetado na URL.

**4. Acesso Root (Sucesso OU Falha)**
```bash
grep -E "(Accepted|Failed).*root" auth.log
```
*Explicação:* Regex procura por "Accepted" ou "Failed" seguidos por qualquer coisa `.*` e depois "root".

**5. Comandos Proibidos (Sudo)**
```bash
grep "command not allowed" auth.log | grep -oP "COMMAND=\K.*"
```
*Explicação:* `-oP` usa Perl Regex. `\K` descarta tudo antes dele no match, imprimindo apenas o comando após `COMMAND=`.

**6. Correlação de IPs (Interseção)**
```bash
comm -12 <(grep -oE "^[0-9.]+" access.log | sort -u) <(grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" auth.log | sort -u)
```
*Explicação:* `comm` compara dois arquivos ordenados. `-12` suprime colunas 1 e 2, mostrando apenas as linhas comuns (interseção). Usa *process substitution* `<( )`.

**7. Horário de pico**
```bash
grep -oP "\d{2}(?=:[0-9]{2}:[0-9]{2})" access.log | sort | uniq -c
```
*Explicação:* Usa *lookahead* `(?=...)` para pegar os 2 dígitos da hora que são seguidos por `:MM:SS`, sem incluir os minutos no match.

**8. User Agents Suspeitos (Não Mozilla)**
```bash
grep -v "Mozilla/5.0" access.log | grep -oP '"[^"]*"$'
```
*Explicação:* Primeiro `grep -v` remove linhas com Mozilla. O segundo extrai a última string entre aspas (User Agent).

**9. Extração de Credenciais (Valor)**
```bash
grep -E "(password|api_key)" config.ini | sed 's/.*= *//'
```
*Explicação:* `grep` acha as linhas. `sed` substitui tudo até o `=` e espaços seguintes por nada, sobrando só o valor.

**10. Validação de Email**
```bash
grep -oE "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" config.ini
```
*Explicação:* Regex robusta para emails. `-o` imprime só o email, não a linha inteira.

**11. Palavras Duplicadas (Backreference)**
```bash
grep -P "\b(\w+)\s+\1\b" *.log
```
*Explicação:* `(\w+)` captura uma palavra. `\s+` exige espaço. `\1` exige que a mesma palavra capturada se repita. `\b` garante limite de palavra.

**12. Lookaround (Status HTTP)**
```bash
grep -oP '"\s\K[0-9]{3}(?=\s)' access.log
```
*Explicação:* `"\s` procura aspas e espaço. `\K` reseta o match (ignora o antes). `[0-9]{3}` pega o status. `(?=\s)` garante que tem um espaço depois (lookahead).

**13. IPv4 Estrito (Validação)**
```bash
grep -P "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$" access.log
```
*Explicação:* Regex complexa que valida faixas 0-255 para cada octeto. Nota: No log real, o IP não está sozinho na linha, então removeria `^` e `$` para buscar no meio da linha.
*Versão para buscar no meio da linha:*
```bash
grep -oP "\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b" access.log
```

**14. Conteúdo entre Delimitadores (Requisição)**
```bash
grep -oP '"\K[^"]+(?=")' access.log | head -5
```
*Explicação:* `\K` ignora a aspa inicial. `[^"]+` pega tudo que não é aspa. `(?=")` garante que termina com aspa.

**15. Versão Semântica (Simulação)**
```bash
echo "Versão v1.2.3 estabilizada" | grep -oP "v\K\d+\.\d+\.\d+"
```
*Explicação:* Captura padrão X.Y.Z após um 'v'. `\d` é dígito no modo Perl.

**16. Comentários ou Vazias**
```bash
grep -cE "^#|^$" config.ini
```
*Explicação:* `^#` começa com #. `^$` linha vazia. `-c` conta.

**17. Negativa Complexa (GET sem 200 sem css/png)**
```bash
grep "GET" access.log | grep -v "200" | grep -vE "css|png"
```
*Explicação:* Pipeline de exclusões sucessivas. Mais legível que uma regex negativa complexa.

**18. Extração de Portas**
```bash
grep -oP "port \K\d+" auth.log
```
*Explicação:* Simples e eficaz com `\K`.

**19. Formato de Data (Convertendo / para -)**
```bash
grep -oP "\d{2}/\w{3}/\d{4}" access.log | sed 's/\//-/g'
```
*Explicação:* `grep` extrai a data. `sed` substitui globalmente `/` por `-`.

**20. Relatório de Auditoria (One-Liner)**
```bash
echo "Total: $(wc -l < access.log), Erros 5xx: $(grep -c '" 5[0-9]{2} ' access.log), IPs Únicos: $(grep -oE '^[0-9.]+' access.log | sort -u | wc -l)"
```
*Explicação:* Combina contagem de linhas, grep count específico e contagem de IPs únicos em uma string formatada.

---

### 💡 Dicas para Nível Especialista

1.  **`grep -P` (Perl Compatible Regex):** Habilita recursos poderosos como *lookarounds* (`(?=...)`, `(?<=...)`), `\K` (reset de match) e `\d` (dígitos). Nem todo `grep` suporta (macOS precisa do `grep` via brew), mas no Linux GNU é padrão.
2.  **`--color=always`:** Útil quando você encadeia grep com grep. O primeiro grep colore, o segundo pode filtrar baseado na cor (usando `grep --color=always ... | grep --color=never ...`).
3.  **Performance:** Em arquivos de gigabytes, `grep` é rápido, mas `sort | uniq` pode consumir muita memória. Use `sort -u` com cuidado em streams infinitos.
4.  **Segurança:** Nunca use `grep` para parsear HTML complexo ou dados estruturados críticos (use `jq` para JSON, `xmlstarlet` para XML). O `grep` é para texto plano e logs.
5.  **Aliases:** Crie aliases no `.bashrc` para buscas comuns, ex: `alias grepp='grep -P --color=auto'`.