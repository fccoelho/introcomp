# Usando o Terminal no Windows
O sistema operacional Windows possui um terminal próprio chamado de `Prompt de Comando` ou `cmd`. No entanto, o `cmd` é um terminal limitado e com poucas funcionalidades. Por isso, muitos desenvolvedores preferem utilizar o terminal do Linux no Windows.

## Instalando o Windows Subsystem for Linux (WSL)
O WSL é uma camada de compatibilidade para rodar aplicativos Linux binários no Windows. Ele é composto por um kernel do Linux, um conjunto de ferramentas de sistema e um ambiente de linha de comando. O WSL 2 é a versão mais recente do WSL e é recomendado para a maioria dos usuários.

Para instalar o WSL 2, siga os passos abaixo:
1. Abra o PowerShell como administrador
2. Execute o seguinte comando:
```powershell
wsl --install
```
3. Reinicie o computador
4. Após reiniciar, abra a Microsoft Store e procure por `Linux`
5. Escolha a distribuição Linux de sua preferência e clique em `Instalar`
6. Após a instalação, abra a distribuição Linux e siga as instruções para criar um usuário e senha
7. Pronto! Agora você pode utilizar o terminal do Linux no Windows
