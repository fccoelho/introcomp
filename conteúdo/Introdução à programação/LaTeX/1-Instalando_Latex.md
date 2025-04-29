# Instalando o LaTeX no Ubuntu
O LaTeX é um sistema de preparação de documentos de alta qualidade, muito utilizado na produção de documentos científicos. Para instalá-lo no Ubuntu, execute os seguintes comandos:

```bash
sudo apt update
sudo apt upgrade
sudo apt install texlive-base texlive-binaries texlive-lang-portuguese
```

Com isso você terá o LaTeX instalado em seu sistema. Para verificar se a instalação foi bem sucedida, execute o comando `pdflatex --version`.

## Instalando o Texstudio
O Texstudio é um editor de LaTeX que facilita a edição de documentos. Para instalá-lo no Ubuntu, execute os seguintes comandos:

```bash 
sudo apt update
sudo apt install texstudio
```
Com isso você terá o Texstudio instalado em seu sistema.

## Instalando a extensão para LaTeX no VSCode

O Visual Studio Code é um editor de código-fonte muito popular e possui uma extensão para LaTeX que facilita a edição de documentos. Para instalá-la, siga os seguintes passos: 
1. Abra o Visual Studio Code.
2. Clique no ícone de extensões na barra lateral esquerda (ou pressione `Ctrl+Shift+X`).
3. Pesquise por "LaTeX Workshop".
4. Clique em "Instalar" na extensão "LaTeX Workshop" de James Yu.
5. Após a instalação, reinicie o Visual Studio Code.
