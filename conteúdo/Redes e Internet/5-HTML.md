# Aprendendo a programar em HTML

## Introdução
O HTML (HyperText Markup Language) é uma linguagem de marcação utilizada para criar páginas web. O HTML é a base de todas as páginas web, e é utilizado para definir a estrutura e o conteúdo de uma página web. O HTML é composto por uma série de elementos, que são utilizados para definir o conteúdo da página, como títulos, parágrafos, imagens, links, entre outros.

## Estrutura de um documento HTML
Um documento HTML é composto por uma série de elementos, que são utilizados para definir a estrutura e o conteúdo da página. Um documento HTML é composto por uma série de elementos, que são utilizados para definir a estrutura e o conteúdo da página. Abaixo está um exemplo de um documento HTML básico.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Título da Página</title>
</head>
<body>
    <h1>Título da Página</h1>
    <p>Este é um parágrafo.</p>
</body>
</html>
```

Vá no [editor online](https://www.w3schools.com/html/html_editor.asp) e digite o código acima. Clique em "Run" para visualizar o resultado.

### Elementos HTML Mais Comuns
Abaixo estão listados alguns dos elementos HTML mais comuns, que são utilizados para definir o conteúdo de uma página web.
1. `<!DOCTYPE html>`: Define o tipo de documento HTML.
2. `<html>`: Define o elemento raiz do documento HTML.
3. `<head>`: Define o cabeçalho do documento HTML.
4. `<title>`: Define o título da página.
5. `<body>`: Define o corpo do documento HTML.
6. `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`: Define os títulos da página.
7. `<p>`: Define um parágrafo.
8. `<a>`: Define um link.
9. `<img>`: Define uma imagem.
10. `<ul>`, `<ol>`, `<li>`: Define listas não ordenadas e ordenadas.
11. `<table>`, `<tr>`, `<td>`, `<th>`: Define uma tabela.
12. `<form>`, `<input>`, `<button>`, `<select>`, `<option>`, `<textarea>`: Define um formulário.
13. `<div>`, `<span>`: Define divisões e spans.
14. `<br>`: Define uma quebra de linha.
15. `<hr>`: Define uma linha horizontal.
16. `<strong>`, `<em>`, `<b>`, `<i>`: Define texto em negrito e itálico.

## Exercícios
1. Crie um documento HTML com um título e um parágrafo.
2. Crie um documento HTML com uma lista não ordenada e uma lista ordenada.
3. Crie um documento HTML com uma tabela.
4. Crie um documento HTML com um formulário.
5. Crie um documento HTML com uma imagem e um link.

## Introdução ao CSS
O [CSS (Cascading Style Sheets)](https://www.w3schools.com/css/) é uma linguagem de estilo utilizada para definir a aparência e o layout de uma página web. O CSS é utilizado para definir estilos como cores, fontes, tamanhos, margens, entre outros. O CSS é composto por uma série de regras, que são utilizadas para definir estilos para os elementos HTML.

### Estrutura de uma regra CSS
Uma regra CSS é composta por um seletor e um bloco de declarações. O seletor é utilizado para selecionar os elementos HTML aos quais a regra se aplica, e o bloco de declarações é utilizado para definir os estilos para os elementos selecionados. Abaixo está um exemplo de uma regra CSS básica.

```css
h1 {
    color: red;
    font-size: 24px;
}
```
### Seletores CSS Mais Comuns
Abaixo estão listados alguns dos seletores CSS mais comuns, que são utilizados para selecionar os elementos HTML aos quais as regras se aplicam.
1. `elemento`: Seleciona todos os elementos do tipo `elemento`.
2. `.classe`: Seleciona todos os elementos com a classe `classe`.
3. `#id`: Seleciona o elemento com o id `id`.
4. `elemento.classe`: Seleciona todos os elementos do tipo `elemento` com a classe `classe`.
5. `elemento#id`: Seleciona o elemento do tipo `elemento` com o id `id`.
6. `elemento1 elemento2`: Seleciona todos os elementos `elemento2` que são descendentes de `elemento1`.
7. `elemento1 > elemento2`: Seleciona todos os elementos `elemento2` que são filhos diretos de `elemento1`.
8. `elemento1 + elemento2`: Seleciona o elemento `elemento2` que é adjacente ao `elemento1`.
9. `elemento1 ~ elemento2`: Seleciona todos os elementos `elemento2` que são irmãos de `elemento1`.

### Exemplos de uso de diferentes seletores CSS
```css
/* Seleciona todos os elementos h1 */
h1 {
    color: red;
    font-size: 24px;
}

/* Seleciona todos os elementos com a classe .paragrafo */
.paragrafo {
    color: blue;
    font-size: 16px;
}

/* Seleciona o elemento com o id #titulo */
#titulo {
    color: green;
    font-size: 32px;
}

/* Seleciona todos os elementos p que são descendentes de h1 */
h1 p {
    color: orange;
    font-size: 12px;
}
```

## Exercícios
1. Crie um documento HTML com um título e um parágrafo, e defina estilos para o título e o parágrafo utilizando CSS.
2. Crie um documento HTML com uma lista não ordenada e uma lista ordenada, e defina estilos para as listas utilizando CSS.
3. Crie um documento HTML com uma tabela, e defina estilos para a tabela utilizando CSS´.
4. Crie um documento HTML com um formulário, e defina estilos para o formulário utilizando CSS.
5. Crie um documento HTML com a estrutura necessária para utilizar o seletores CSS mais comuns, listados acima.


## Referências
- [HTML - Wikipedia](https://en.wikipedia.org/wiki/HTML)
- [HTML - W3Schools](https://www.w3schools.com/html/)
- [HTML - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML)

