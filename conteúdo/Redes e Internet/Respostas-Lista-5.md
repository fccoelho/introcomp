1. HTML (Hypertext Markup Language) é uma linguagem de marcação usada para criar páginas web. É o acrônimo de 'Hypertext Markup Language'.
2. Uma tag HTML é uma directive que determina como um navegador deve renderizar um texto ou outra informação no documento. Por exemplo, as tags <h1> e <p>.
3. Um atributo em HTML é uma chave: valor pares que descreve um aspecto de um elemento. Exemplos incluem o 'class' e 'id' atributos.
4. Um elemento HTML é basicamente tudo que está dentro de um parâmetro '< >'. Isso pode ser um texto, outro elemento ou até mesmo um formulário. Um exemplo é <form>.
5. Um documento mínimo em HTML:
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Título da Página</title>
</head>
<body>

<h1>Minha primeira página</h1>

<p>Este é um parágrafo.</p>

</body>
</html>
```
6. As principais seções de um documento HTML incluem head e body.
7. Um formulário HTML com campos de texto, caixas de seleção, botões de rádio e botões de envio poderia parecer:
```html
<form action="/submit_form" method="post">
  <label for="fname">First Name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <input type="radio" id="male" name="gender" value="male">
  <label for="male">Male</label><br>
  <input type="radio" id="female" name="gender" value="female">
  <label for="female">Female</label><br>
  <input type="submit" value="Submit">
</form>
```
8. Você pode adicionar estilos a elementos HTML usando CSS (Cascading Style Sheets).
9. CSS (Cascading Style Sheets) é uma linguagem de estilo usada para controlar o visual do conteúdo HTML. É o acrônimo de 'Cascading Style Sheets'.
10. Um seletor CSS é um caminho que você usa para localizar as propriedades CSS específicas para aplicar a eles. Exemplos incluem seletores de classe, ID e atributos.
11. Você pode carregar um arquivo CSS em um documento HTML usando a tag <link>. Por exemplo:
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Page Title</title>
<link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>

<h1>My First Page</h1>

<p>This is a paragraph.</p>

</body>
</html>
```
