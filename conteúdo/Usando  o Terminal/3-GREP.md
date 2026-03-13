# O aplicativo GREP - Guia Estendido para Iniciantes

O [GREP](https://en.wikipedia.org/wiki/Grep) é um aplicativo que permite a busca de padrões em arquivos de texto. Ele é uma das ferramentas mais poderosas e utilizadas em sistemas Unix/Linux, essencial para qualquer profissional de Ciência de Dados que precise explorar, limpar ou analisar dados diretamente no terminal.

**Por que aprender GREP?**
- 🔍 Encontrar rapidamente informações em arquivos grandes (logs, CSVs, JSON)
- 🧹 Filtrar dados relevantes para análise
- ⚡ Processar texto sem precisar abrir editores ou importar para Python/R
- 🔗 Combinar com outras ferramentas (`| pipe`) para criar fluxos de processamento

Ele se utiliza de **expressões regulares** para realizar a busca, o que torna suas possibilidades quase ilimitadas.

---

## Introdução às Expressões Regulares (Para Iniciantes)

> 💡 **Pense em expressões regulares como "receitas de busca"**: você descreve o padrão do que quer encontrar, e o computador faz o trabalho pesado.

Uma [expressão regular](https://en.wikipedia.org/wiki/Regular_expression) é uma sequência de caracteres que especifica um padrão de busca. Para alunos de primeiro período, vamos focar nos conceitos essenciais:

### 1. Caracteres Literais (O Básico)
São os caracteres que você deseja encontrar exatamente como estão escritos.

```bash
# Buscar a palavra "dados" em um arquivo
$ grep "dados" relatorio.txt
```

### 2. Metacaracteres Fundamentais
Metacaracteres são símbolos especiais que dão "superpoderes" à sua busca.

| Metacaractere | Significado | Exemplo | O que encontra |
|--------------|-------------|---------|---------------|
| `.` | Qualquer caractere único | `c.sa` | casa, cosa, c@sa, c#sa |
| `*` | Zero ou mais repetições do anterior | `ab*c` | ac, abc, abbc, abbbc |
| `^` | Início da linha | `^Inicio` | Linhas que começam com "Inicio" |
| `$` | Fim da linha | `fim$` | Linhas que terminam com "fim" |
| `[]` | Qualquer caractere dentro dos colchetes | `[aeiou]` | Qualquer vogal |
| `[^]` | Qualquer caractere **exceto** os listados | `[^0-9]` | Qualquer coisa que não seja dígito |
| `?` | Zero ou uma ocorrência (opcional) | `colou?r` | color ou colour |
| `+` | Uma ou mais ocorrências | `ab+c` | abc, abbc (mas NÃO ac) |
| `|` | OU lógico | `gato\|cachorro` | gato ou cachorro |
| `()` | Agrupamento | `(ab)+` | ab, abab, ababab |

> ⚠️ **Atenção**: Alguns metacaracteres precisam de "escape" com `\` para funcionarem como caracteres literais. Ex: para buscar um ponto literal, use `\.`

### 3. Classes de Caracteres (Atalhos Úteis)
Para facilitar, existem atalhos para padrões comuns:

| Atalho | Significado | Equivalente |
|--------|-------------|-------------|
| `\d` ou `[0-9]` | Qualquer dígito | `[0123456789]` |
| `\w` | Caractere de palavra (letras, dígitos, underscore) | `[a-zA-Z0-9_]` |
| `\s` | Espaço em branco (espaço, tab, nova linha) | `[ \t\n\r]` |
| `\b` | Borda de palavra (início ou fim) | - |

> 📝 **Nota para Bash**: No `grep` padrão, use `-E` para expressões estendidas ou `egrep` para habilitar atalhos como `\d`.

---

## Usando o GREP: Exemplos Práticos

### 🔹 Busca Básica
```bash
# Encontrar todas as linhas com a palavra "erro" em um log
$ grep "erro" sistema.log

# Buscar ignorando maiúsculas/minúsculas (-i)
$ grep -i "erro" sistema.log
# Encontra: erro, Erro, ERRO, eRrO...
```

### 🔹 Busca com Contexto
Muito útil para entender o que acontece antes/depois de um padrão:
```bash
# Mostrar 2 linhas antes e depois da ocorrência (-C)
$ grep -C 2 "erro" sistema.log

# Mostrar apenas 3 linhas depois (-A)
$ grep -A 3 "erro" sistema.log

# Mostrar apenas 3 linhas antes (-B)
$ grep -B 3 "erro" sistema.log
```

### 🔹 Contando e Numerando
```bash
# Contar quantas linhas contêm o padrão (-c)
$ grep -c "usuario" acesso.log
# Saída: 42

# Mostrar o número da linha onde o padrão foi encontrado (-n)
$ grep -n "login" acesso.log
# Saída: 15:usuario123 realizou login
#        89:usuario456 realizou login
```

### 🔹 Busca Invertida e Arquivos Múltiplos
```bash
# Mostrar linhas que NÃO contêm o padrão (-v)
$ grep -v "DEBUG" app.log
# Útil para filtrar ruído e focar em erros/warnings

# Buscar em múltiplos arquivos
$ grep "conexao" *.log
# Saída: servidor.log:conexao estabelecida
#        banco.log:conexao perdida

# Buscar recursivamente em subdiretórios (-r)
$ grep -r "senha" ./configuracoes/
```

### 🔹 Expressões Regulares no GREP

#### Ancoragem: Início e Fim de Linha
```bash
# Linhas que COMEÇAM com "ERROR"
$ grep "^ERROR" sistema.log

# Linhas que TERMINAM com "falha"
$ grep "falha$" sistema.log

# Linhas que são EXATAMENTE "OK" (nada antes, nada depois)
$ grep "^OK$" status.txt
```

#### Caracteres Curinga e Repetições
```bash
# Buscar padrões como "user1", "user2", "user99"
$ grep "user[0-9]" acesso.log

# Buscar e-mails simples (exemplo didático)
$ grep -E "[a-z]+@[a-z]+\.[a-z]+" contatos.txt

# Buscar palavras com 3 ou mais repetições de uma letra
$ grep -E "a{3,}" texto.txt
# Encontra: aaa, aaaa, baaac...
```

#### Agrupamento e Alternância
```bash
# Buscar "Brasil" ou "Brazil" (com ou sem z)
$ grep -E "Braz?il" paises.txt

# Buscar padrões como "erro crítico" ou "erro fatal"
$ grep -E "erro (crítico|fatal)" sistema.log

# Buscar datas no formato DD/MM/AAAA
$ grep -E "[0-9]{2}/[0-9]{2}/[0-9]{4}" relatorio.csv
```

### 🔹 Opções Avançadas Úteis
```bash
# Apenas mostrar o padrão encontrado, não a linha inteira (-o)
$ grep -o "[0-9]\+\.[0-9]\+" dados.csv
# Saída: 3.14
#        2.71
#        1.41

# Contar ocorrências do padrão, não apenas linhas
$ grep -o "erro" sistema.log | wc -l

# Buscar apenas nomes de arquivos que contêm o padrão (-l)
$ grep -l "conexao" *.log
# Saída: servidor.log
#        banco.log
```

---

## Casos Práticos para Ciência de Dados

### 📊 Filtrando Dados CSV
```bash
# Extrair apenas linhas de um país específico em um CSV
$ grep "^Brasil," dados_mundial.csv

# Encontrar valores ausentes (campos vazios entre vírgulas)
$ grep ",," dados.csv

# Buscar valores numéricos acima de um limite (exemplo simplificado)
$ grep -E ",[0-9]{4,}," vendas.csv
# Encontra valores com 4+ dígitos
```

### 🔐 Analisando Logs de Acesso
```bash
# Contar tentativas de login por usuário
$ grep "login" acesso.log | grep -o "usuario[0-9]*" | sort | uniq -c

# Encontrar IPs com múltiplas tentativas falhas
$ grep "falha" acesso.log | grep -o "[0-9]\+\.[0-9]\+\.[0-9]\+\.[0-9]\+" | sort | uniq -c | sort -nr

# Filtrar logs por horário (ex: apenas entre 14:00 e 15:00)
$ grep -E "14:[0-5][0-9]:" acesso.log
```

### 🧹 Pré-processamento de Texto
```bash
# Remover linhas vazias de um arquivo
$ grep -v "^$" texto.txt > texto_limpo.txt

# Extrair apenas linhas com conteúdo útil (que tenham pelo menos uma letra)
$ grep "[a-zA-Z]" dados_brutos.txt

# Encontrar duplicatas em uma lista
$ sort lista.txt | grep -E "^(.*)$\n\1" 
# (Nota: para duplicatas exatas, combine com uniq)
```

---

## Combinando GREP com Outras Ferramentas

### Com `sort` e `uniq` para análise
```bash
# Contar frequência de palavras em um texto
$ grep -o -E "\b[a-zA-Z]+\b" texto.txt | sort | uniq -c | sort -nr | head -20

# Extrair e contar domínios de e-mails
$ grep -o -E "[a-z]+@[a-z]+\.[a-z]+" contatos.txt | cut -d@ -f2 | sort | uniq -c
```

### Com `cut` para extrair colunas
```bash
# Filtrar linhas E extrair colunas específicas
$ grep "Brasil" dados.csv | cut -d, -f1,3,5

# Buscar por padrão e depois selecionar campo
$ grep "ERROR" log.txt | cut -d" " -f3-
```

### Com `sed` para substituição + busca
```bash
# Substituir padrão e depois filtrar
$ sed 's/old/new/g' arquivo.txt | grep "new"

# Contar ocorrências após normalização
$ sed 's/[0-9]//g' dados.txt | grep -c "padrao"
```

### Com pipes para fluxos complexos
```bash
# Pipeline: filtrar → extrair → contar → ordenar
$ grep "2024" vendas.csv | \
  grep -o -E "[0-9]+,[0-9]{2}" | \
  cut -d, -f2 | \
  sort -n | \
  uniq -c
```

---

## Alternativas e Complementos ao GREP

### O comando `awk`
O `awk` é excelente para processamento estruturado (como CSVs):

```bash
# Extrair colunas específicas de um CSV
$ awk -F, '{print $1, $4}' dados.csv

# Filtrar por condição numérica
$ awk -F, '$5 > 1000 {print $0}' vendas.csv

# Combinar grep + awk para poder total
$ grep "Brasil" dados.csv | awk -F, '{print $3}'
```

### O comando `sed`
Para substituições e edições em fluxo:

```bash
# Substituir todas as ocorrências
$ sed 's/antigo/novo/g' arquivo.txt

# Apagar linhas que contêm padrão
$ sed '/DEBUG/d' log.txt

# Extrair apenas linhas que casam com padrão
$ sed -n '/ERROR/p' log.txt
```

### O comando `tr`
Para tradução e limpeza de caracteres:

```bash
# Converter maiúsculas para minúsculas
$ tr 'A-Z' 'a-z' < texto.txt

# Remover caracteres indesejados
$ tr -d '\r' < arquivo_dos.txt > arquivo_unix.txt

# Substituir delimitadores
$ tr ',' ';' < dados.csv > dados_separado_ponto_virgula.csv
```

### O comando `cut`
Para extração simples de colunas:

```bash
# Extrair primeiras 3 colunas de um CSV
$ cut -d, -f1-3 dados.csv

# Extrair colunas específicas
$ cut -d, -f1,4,7 dados.csv

# Extrair por posição de caractere (útil para formatos fixos)
$ cut -c1-10,20-30 arquivo.txt
```

### O `ripgrep` (`rg`) - O grep moderno
Mais rápido e com sintaxe amigável:

```bash
# Instalação (Ubuntu/Debian)
$ sudo apt install ripgrep

# Busca básica (sintaxe similar, mas mais intuitiva)
$ rg "erro" sistema.log

# Busca case-insensitive por padrão
$ rg -i "erro" sistema.log

# Ignorar arquivos .git e node_modules automaticamente
$ rg "padrao" ./projeto

# Mostrar contexto com cores
$ rg -C 3 "conexao" *.log
```

> 🚀 **Dica**: O `ripgrep` é excelente para projetos grandes e busca recursiva. Para scripts portáteis, prefira `grep` que está em todo sistema Unix.

---

## Exercícios Práticos

### 🎯 Nível Iniciante
1. Crie um arquivo `teste.txt` com 10 linhas misturando palavras como "dados", "analise", "python", "R".
2. Use `grep` para:
   - Encontrar todas as linhas com "dados"
   - Contar quantas linhas têm "python"
   - Mostrar linhas que NÃO contêm "R"
   - Buscar linhas que começam com "A"

### 🎯 Nível Intermediário
3. Baixe um arquivo de log de exemplo ou crie um com padrões de data, IP e mensagens.
4. Pratique:
   ```bash
   # Extrair todos os endereços IP do log
   $ grep -o -E "[0-9]{1,3}(\.[0-9]{1,3}){3}" acesso.log
   
   # Filtrar logs apenas do horário comercial (9h-18h)
   $ grep -E "(0[9-9]|1[0-7]):[0-5][0-9]:" acesso.log
   
   # Contar ocorrências de cada nível de log (INFO, WARN, ERROR)
   $ grep -o -E "(INFO|WARN|ERROR)" sistema.log | sort | uniq -c
   ```

### 🎯 Nível Desafio (Ciência de Dados)
5. Trabalhe com um dataset CSV simples (ex: dados de vendas):
   ```bash
   # Filtrar vendas acima de R$ 1000
   $ awk -F, '$4 > 1000 {print $0}' vendas.csv
   
   # Extrair nomes de clientes que compraram em 2024
   $ grep "2024" vendas.csv | cut -d, -f2 | sort -u
   
   # Gerar relatório: contar vendas por região
   $ cut -d, -f3 vendas.csv | sort | uniq -c | sort -nr
   ```

6. **Desafio criativo**: Crie um pipeline que:
   - Leia um arquivo de texto
   - Remova linhas vazias e comentários (que começam com #)
   - Extraia apenas palavras com mais de 5 letras
   - Conte a frequência das 10 palavras mais comuns

---

## Dicas Finais para Primeiranistas

✅ **Comece simples**: Domine buscas literais antes de usar regex complexas  
✅ **Teste em arquivos pequenos**: Crie arquivos de teste antes de rodar em dados reais  
✅ **Use `-i` para evitar frustrações**: Maiúsculas/minúsculas pegam muitos iniciantes  
✅ **Combine ferramentas**: `grep | cut | sort | uniq` é uma sequência poderosa  
✅ **Consulte o manual**: `man grep` ou `grep --help` são seus amigos  
✅ **Pratique com dados reais**: Use logs do sistema, CSVs de exercícios, ou dados públicos  

> 🎓 **Lembrete**: Expressões regulares são como andar de bicicleta — estranho no início, mas depois se torna natural. Não desista nos primeiros erros!

---

## Recursos para Aprofundamento

- 🌐 [Regex101](https://regex101.com/) - Teste expressões regulares visualmente
- 📚 [RegexOne](https://regexone.com/) - Tutorial interativo para iniciantes
- 🐧 [Explainshell](https://explainshell.com/) - Entenda comandos bash complexos
- 📦 [GNU Grep Manual](https://www.gnu.org/software/grep/manual/grep.html) - Documentação oficial

---

## Gabarito Sugerido (para o instrutor)

<details>
<summary>▶️ Clique para ver respostas dos exercícios</summary>

**Exercício 2:**
```bash
grep "dados" teste.txt
grep -c "python" teste.txt
grep -v "R" teste.txt
grep "^A" teste.txt
```

**Exercício 4 (contagem de níveis):**
```bash
# Saída exemplo:
#     45 ERROR
#    128 INFO
#     37 WARN
```

**Exercício 6 (pipeline criativo):**
```bash
cat texto.txt | \
  grep -v "^#" | \
  grep -v "^$" | \
  grep -o -E "\b[a-zA-Z]{6,}\b" | \
  tr 'A-Z' 'a-z' | \
  sort | uniq -c | sort -nr | head -10
```

</details>