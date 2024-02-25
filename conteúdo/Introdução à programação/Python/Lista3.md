# Interagindo com código externo, usando o `import`

Para realizar os exercícios seguintes, instale faça um clone local do projeto [autoreport](https://github.com/fccoelho/autoreport) desenvolvido em sala de aula.

Crie um ambiente virtual para o projeto e instale o autoreport nele:

```bash
$ cd autoreport
$ poetry install
$ poetry shell
```
Responda os problemas a seguir em um módulo chamado `meurelatorio.py` na raiz do projeto epireport. Cada problema exigirá implementar uma função neste módulo

1. Crie uma função denominada `gera_relatorio_vazio`, que deverá salvar um arquivo `relatorio.tex` somente com o conteúdo do template. Pode utilizar qualquer string para o título e o autor do relatório. Esta função também deve retornar uma string correspondente ao código LaTeX gerado.
2. Crie uma função denominada `gera_relatorio_secoes`, que receba como argumento uma lista de `n` (n > 1) títulos, de seções, e salve um relatório com as `n` seções, cada uma com o título correspondente. Esta função também deve retornar uma tupla com dois elementos: o primeiro deve ser a lista de títulos passada como argumento, e o segundo uma string correspondente ao código LaTeX gerado. O nome do relatório gerado deve ser `relatorio_secoes.tex`.
3. Crie uma função denominada `gera_relatorio_tabela`, que receba como argumento uma lista de listas, onde cada lista interna corresponde a uma linha de uma tabela. Esta função deve salvar um relatório com uma tabela (em latex) contendo as linhas passadas como conteúdo. Esta função também deve retornar uma tupla com dois elementos: o primeiro deve ser a lista de listas passada como argumento, e o segundo uma string correspondente ao código LaTeX gerado. O nome do relatório gerado deve ser `relatorio_tabela.tex`. Utilize o template de tabela abaixo:

```latex
\begin{table}
\begin{center}
\caption{Tabela de resultados}
\begin{tabular}{lll}
1 & 2 & 3\\
4 & 5 & 6\\
× & × & ×
\end{tabular}
\end{center}
\end{table}
```
O número de colunas ou linhas pode variar.
A tabela deve ser parte de uma seção denominada `Resultados`.