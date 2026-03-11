# Software

Software é definido como um conjunto que inclui [programas de computador](https://en.wikipedia.org/wiki/Computer_program), sua documentação e seus dados [[1]]. Mais especificamente, software consiste em programas de computador que instruem a execução de um computador, incluindo também documentos de design e especificações [[3]]. A documentação do software é o texto escrito ou ilustrações que acompanham o software ou estão incorporadas ao código-fonte, fornecendo informações essenciais para desenvolvedores, testadores e usuários [[8]].

## Tipos

Softwares podem ser categorizados em diferentes tipos conforme sua função e propósito:

![Classificação de Software](https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Operating_system_placement_%28software%29.svg/960px-Operating_system_placement_%28software%29.svg.png)

**Figura 1:** Classificação hierárquica dos principais tipos de software

### 1. Softwares de Sistema

O software de sistema é projetado principalmente para executar o hardware do computador e gerenciar recursos do sistema. Ele tipicamente inclui sistemas operacionais, drivers de dispositivo, programas utilitários e tradutores de linguagem como compiladores e assemblers.

#### 1.1 BIOS
A [BIOS (Basic Input/Output System)](https://en.wikipedia.org/wiki/BIOS) é um tipo de firmware usado para fornecer serviços de runtime para sistemas operacionais e programas, além de realizar a inicialização do hardware durante o processo de boot.

#### 1.2 Sistemas Operacionais
Um [sistema operacional (SO)](https://en.wikipedia.org/wiki/Operating_system) é software de sistema que gerencia recursos de hardware e software do computador e fornece serviços comuns para programas de computador. Exemplos incluem Windows, Linux, macOS, Android e iOS.

#### 1.3 Drivers
[Drivers de dispositivo](https://en.wikipedia.org/wiki/Device_driver) são softwares de sistema que permitem que o sistema operacional se comunique com dispositivos de hardware. Cada dispositivo requer um driver específico para funcionar corretamente.

#### 1.4 Utilitários
[Programas utilitários](https://en.wikipedia.org/wiki/Utility_software) são ferramentas que auxiliam na manutenção, configuração e otimização do sistema. Incluem antivírus, ferramentas de backup, gerentes de arquivos e utilitários de diagnóstico.

### 2. Aplicativos

[Software aplicativo](https://en.wikipedia.org/wiki/Application_software) é projetado para realizar tarefas específicas para o usuário final, como processamento de texto, planilhas, navegação na web, edição de imagens, entre outros.

### 3. Programas de Usuários

São programas desenvolvidos por usuários ou organizações para atender necessidades específicas, podendo incluir scripts, macros e aplicações personalizadas.

![Software Stack](https://upload.wikimedia.org/wikipedia/commons/d/d4/Layers_of_a_Linux_system.png)

**Figura 2:** Posicionamento do sistema operacional na pilha de software

Podemos acrescentar à lista acima a categoria de [Malware](https://en.wikipedia.org/wiki/Malicious_software), que são softwares projetados para fins maliciosos, como vírus, worms, trojans, ransomware e spyware. Mas estes não serão objeto de estudo do nosso curso.

## Domínio de Execução

Os softwares podem ser qualificados em domínios de execução, ou seja, qual ambiente é necessário para a sua execução:

![Execution Environment](https://image.qwenlm.ai/public_source/0392da38-a979-46d5-8b6e-7b6a6ac66a6b/2154617e7-675d-4b67-a1d8-55fa889fa0053501.png)

**Figura 3:** Componentes de um ambiente de execução de software

### 1. O Browser

O navegador web é um ambiente de execução para aplicações web client-side. A [Linguagem JavaScript](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript) foi criada especificamente para desenvolver softwares que sejam executados dentro do browser, permitindo interatividade e dinamismo às páginas web.

### 2. [Aplicações Web](https://en.wikipedia.org/wiki/Web_application)

São aplicações que rodam em servidores web e são acessadas através de navegadores. Utilam arquiteturas em camadas, incluindo camada de apresentação, camada de negócio e camada de dados [[2]].

![Web Application Architecture](https://image.qwenlm.ai/public_source/0392da38-a979-46d5-8b6e-7b6a6ac66a6b/0154617e7-675d-4b67-a1d8-55fa889fa0057264.png)

**Figura 4:** Arquitetura em camadas de uma aplicação web típica

### 3. [Software Embarcado](https://en.wikipedia.org/wiki/Embedded_software)

Software embarcado refere-se a software de computador especificamente projetado para controlar máquinas ou dispositivos que não são tradicionalmente considerados como computadores [[21]]. Um sistema embarcado é um sistema de computador especializado—uma combinação de processador, memória e dispositivos de entrada/saída periféricos [[25]].

Características do software embarcado:
- Executa em hardware com recursos limitados
- Frequentemente opera em tempo real
- Integrado diretamente ao dispositivo
- Exemplos: sistemas automotivos, eletrodomésticos inteligentes, dispositivos médicos, IoT

### 4. [Aplicações para Desktop](https://en.wikipedia.org/wiki/Desktop_application)

São aplicações instaladas e executadas localmente no computador do usuário, oferecendo geralmente maior desempenho e acesso completo aos recursos do sistema operacional.

### 5. Aplicações Móveis

Desenvolvidas especificamente para dispositivos móveis como smartphones e tablets, executando em sistemas operacionais como Android e iOS.

### 6. Aplicações em Nuvem (Cloud)

Software executado em servidores remotos e acessado via internet, seguindo modelos como SaaS (Software as a Service), PaaS (Platform as a Service) e IaaS (Infrastructure as a Service).

## Arquitetura de Software em Camadas

A maioria dos sistemas de software modernos segue uma arquitetura em camadas, onde cada camada tem responsabilidades específicas:

![Layered Architecture](https://image.qwenlm.ai/public_source/0392da38-a979-46d5-8b6e-7b6a6ac66a6b/3154617e7-675d-4b67-a1d8-55fa889fa0054999.png)

**Figura 5:** Padrão de arquitetura em camadas mostrando o fluxo de requisições

**Camadas típicas:**
- **Camada de Apresentação:** Interface com o usuário
- **Camada de Negócio:** Regras e lógica da aplicação
- **Camada de Persistência:** Gerenciamento de dados
- **Camada de Banco de Dados:** Armazenamento físico dos dados

## Referências

1. Wikipedia. Software documentation. Disponível em: https://en.wikipedia.org/wiki/Software_documentation
2. Wikipedia. Software. Disponível em: https://en.wikipedia.org/wiki/Software
3. GeeksforGeeks. Overview Software Documentation. Disponível em: https://www.geeksforgeeks.org/software-engineering/overview-software-documentation/
4. Wikipedia. System software. Disponível em: https://en.wikipedia.org/wiki/System_software
5. Wikipedia. Operating system. Disponível em: https://en.wikipedia.org/wiki/Operating_system
6. Wikipedia. BIOS. Disponível em: https://en.wikipedia.org/wiki/BIOS
7. Wikipedia. Embedded software. Disponível em: https://en.wikipedia.org/wiki/Embedded_software
8. Wikipedia. Embedded system. Disponível em: https://en.wikipedia.org/wiki/Embedded_system
9. Wikipedia. Web application. Disponível em: https://en.wikipedia.org/wiki/Web_application
10. Wikipedia. Desktop application. Disponível em: https://en.wikipedia.org/wiki/Desktop_application

## Figuras

- Figura 1: Software classification diagram
- Figura 2: Operating system placement in software stack (Wikimedia Commons)
- Figura 3: Execution environment components
- Figura 4: Web application layered architecture
- Figura 5: Layered architecture pattern with request flow