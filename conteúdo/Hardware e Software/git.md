# Git, Github e Versionamento:

O Git é um sistema de versionamento distribuído que é usado pela vasta maioria de projetos de desenvolvimento globalmente. O GitHub, é uma aplicação Web que facilita a colaboração em projetos versionados pelo `git`.

## Primeiros passos
Antes de começarmos a usar o `git` temos que fazer uma breve configuração da ferramenta:

O git identifica os desenvolvedores pelo seu nome e email, portanto devemos informar ao git estes dados

```bash
$ git config --global user.name "Fulano de Tal"
$ git config --global user.email fulanodetal@exemplo.br
```


Atualizando o editor padrão do Git bash. (para usuários Windows):
```bash
$ git config --global core.editor "nano.exe"
```
Este comando também funciona para outros sistemas operacionais, bastando modificar o nome do editor desejado.

Existem várias outras configurações possíveis. Mas estas, por hora, são suficientes. Para listar as suas configurações, vc pode usar o seguinte comando:
```bash
$ git config --list
```
## Começando um novo repositório
A unidade de trabalho do `git` é o repositório, que é um diretório (árvore de diretórios) em seu sistema de arquivos, que contém o código a ser versionado.

## Link úteis
- [Tutorial de Git](https://git-scm.com/book/pt-br/v2)
- [Ambiente Interativo](https://learngitbranching.js.org/)
- [Texto introdutório sobre Git](https://www.dadosaleatorios.com.br/post/introdu%C3%A7%C3%A3o-ao-git/)  
- [Outro guia rápido de GIT](http://rogerdudler.github.io/git-guide/index.pt_BR.html)  
- [Curso gratuito de Git e Github](https://www.udemy.com/git-e-github-para-iniciantes/)  
- [Git Cheat Sheet](https://www.git-tower.com/blog/git-cheat-sheet/)  
=======
Git references [intro](https://towardsdatascience.com/introduction-to-github-for-data-scientists-2cf8b9b25fba), [intro (pt-br)](https://git-scm.com/book/pt-br/v1/Primeiros-passos-No%C3%A7%C3%B5es-B%C3%A1sicas-de-Git), [intro2 (pt-br)](https://www.dadosaleatorios.com.br/post/introdu%C3%A7%C3%A3o-ao-git/), [guide](http://rogerdudler.github.io/git-guide/index.pt_BR.html), [course (pt-br)](https://www.udemy.com/git-e-github-para-iniciantes/), [cheat sheet](https://www.git-tower.com/blog/git-cheat-sheet/)  

Configurações:  
  + [Configurando o upstream localmente](https://help.github.com/articles/configuring-a-remote-for-a-fork/)  
  + [Sincronizando um fork de repositório com o upstream](https://help.github.com/articles/syncing-a-fork/)  
  + [Desfazendo um commit](https://blog.github.com/2015-06-08-how-to-undo-almost-anything-with-git/)  
  + [Procurando coisas no repositório](https://www.tygertec.com/find-stuff-git/)  
  + [Resolvendo conflitos no Git](https://stackoverflow.com/questions/161813/how-to-resolve-merge-conflicts-in-git)  
