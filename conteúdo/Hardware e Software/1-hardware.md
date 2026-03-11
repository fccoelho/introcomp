# Hardware

No contexto da computação, a palavra `hardware` se refere aos componentes físicos de um computador, mais especificamente aos componentes eletrônicos e eletromecânicos que estão diretamente ligados à execução de tarefas computacionais. Isso inclui circuitos integrados, placas de circuito impresso (PCBs), componentes de armazenamento, dispositivos de entrada/saída e sistemas de refrigeração. Não se refere a elementos estruturais como 🔩 parafusos e porcas, embora estes façam parte do computador físico.

O hardware moderno é organizado hierarquicamente, seguindo princípios estabelecidos desde meados do século XX, mas continuamente evoluídos para atender às demandas de desempenho, eficiência energética e miniaturização.

![computador pessoal explodido](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Personal_computer%2C_exploded_6.svg/1920px-Personal_computer%2C_exploded_6.svg.png)

*Figura 1: Vista explodida de um computador pessoal mostrando os principais componentes físicos.*

## Principais Componentes 

Assumindo uma arquitetura típica de um computador pessoal atual (2024-2026), podemos encontrar os principais componentes interconectados por meio de uma **placa-mãe** (motherboard), que serve como espinha dorsal do sistema, fornecendo energia, clock e caminhos de comunicação entre todos os dispositivos.

![placa-mae moderna](https://upload.wikimedia.org/wikipedia/commons/b/b7/Computer-motherboard.jpg)

*Figura 2: Placa-mãe ATX moderna mostrando CPU socket, slots de RAM, chipset e conectores de expansão.*

### Componentes da Placa-Mãe

Na placa-mãe encontramos:

#### **CPU (Central Processing Unit) / Processador**
A CPU é o "cérebro" do computador, responsável por executar instruções de programas. Processadores modernos como Intel Core i9-14900K ou AMD Ryzen 9 7950X utilizam arquiteturas de 7nm ou 5nm, contendo bilhões de transistores e múltiplos núcleos (cores) com frequências de clock que variam de 3.0 a 6.0 GHz.

**Características técnicas:**
- **Arquitetura**: x86-64 (Intel/AMD) ou ARM (Apple Silicon, Qualcomm)
- **Núcleos**: De 4 a 64+ núcleos físicos
- **Threads**: Suporte a multithreading simultâneo (SMT/Hyper-Threading)
- **Cache**: Hierarquia L1 (32-128KB), L2 (256KB-2MB), L3 (8-128MB)
- **TDP (Thermal Design Power)**: 65W a 250W+

#### **Chipset**
O chipset é um conjunto de circuitos integrados que gerencia o fluxo de dados entre o processador, memória e periféricos. Em sistemas modernos, o chipset é frequentemente dividido em:
- **PCH (Platform Controller Hub)**: Gerencia USB, SATA, PCIe, áudio e rede
- **Controlador de Memória**: Integrado à CPU em arquiteturas modernas
- **Controlador PCIe**: Gerencia lanes de expansão

#### **Memória RAM (Random Access Memory)**
A memória principal volátil armazena dados e instruções em uso ativo. Tecnologias atuais incluem:

**DDR5 (Double Data Rate 5):**
- Velocidades: 4800 a 8400+ MT/s
- Tensão: 1.1V (mais eficiente que DDR4 @ 1.2V)
- Capacidade: 8GB a 128GB por módulo
- Arquitetura: Dual-channel ou quad-channel

**Características críticas:**
- **Latência**: CL (CAS Latency) de 30-40 ciclos para DDR5
- **Largura de banda**: Até 67+ GB/s por canal
- **ECC (Error Correcting Code)**: Disponível para servidores/workstations

![hierarquia de memoria](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Memory_hierarchy.svg/800px-Memory_hierarchy.svg.png)

*Figura 3: Hierarquia de memória mostrando a relação entre velocidade, capacidade e custo.*

#### **BIOS/UEFI (Basic Input/Output System / Unified Extensible Firmware Interface)**
Firmware armazenado em chip Flash ROM que inicializa o hardware e carrega o sistema operacional. UEFI moderno substituiu a BIOS legada, oferecendo:
- Interface gráfica
- Suporte a discos >2TB (GPT partitioning)
- Secure Boot (verificação criptográfica)
- Network boot e atualizações via internet
- CMOS: Memória volátil alimentada por bateria que armazena configurações (data/hora, boot order)

#### **Slots de Expansão**
- **PCIe (Peripheral Component Interconnect Express)**: 
  - Versões: PCIe 4.0 (16 GT/s), PCIe 5.0 (32 GT/s), PCIe 6.0 (64 GT/s)
  - Configurações: x1, x4, x8, x16 lanes
  - Largura de banda: PCIe 5.0 x16 = ~63 GB/s bidirecional

#### **Placa de Vídeo / GPU (Graphics Processing Unit)**

A GPU pode ser:

**Integrada (iGPU):**
- Incorporada ao die da CPU (Intel UHD Graphics, AMD Radeon Graphics, Apple M-series)
- Compartilha memória RAM do sistema
- Adequada para tarefas básicas e vídeo

**Discreta (dGPU):**
- Placa dedicada com GPU própria e VRAM (Video RAM)
- Tecnologias: NVIDIA GeForce RTX 4090, AMD Radeon RX 7900 XTX
- **VRAM**: GDDR6/GDDR6X de 8GB a 24GB+
- **CUDA Cores / Stream Processors**: Milhares de núcleos paralelos
- **Aplicações**: Gaming, machine learning, renderização 3D, computação científica

![arquitetura GPU](https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Nvidia_GeForce_RTX_2080_Founders_Edition_GPU.jpg/800px-Nvidia_GeForce_RTX_2080_Founders_Edition_GPU.jpg)

*Figura 4: GPU moderna mostrando dissipador de calor e ventiladores.*

### Subsistemas de Armazenamento

#### **SSD (Solid State Drive)**
- **NVMe (Non-Volatile Memory Express)**: Interface PCIe direta
  - Velocidades: 3500-7000+ MB/s (PCIe 4.0/5.0)
  - Form factors: M.2 2280, U.2, add-in card
- **SATA SSD**: 550 MB/s limite teórico
- **Tecnologia NAND**: TLC (Triple-Level Cell), QLC (Quad-Level Cell), 3D stacking (100+ layers)

#### **HDD (Hard Disk Drive)**
- Armazenamento magnético mecânico
- Capacidades: 1TB a 22TB+
- Velocidades: 5400-7200 RPM
- Interface: SATA 6 Gb/s
- Uso: Armazenamento em massa, backup, arquivamento

### Sistemas de Entrada/Saída (I/O)

#### **Portas e Conectores**
- **USB (Universal Serial Bus)**:
  - USB 3.2 Gen 2x2: 20 Gb/s
  - USB4 / Thunderbolt 4: 40 Gb/s
  - USB-C: Conector reversível com suporte a Power Delivery (até 240W)
  
- **Rede**:
  - Ethernet: 1/2.5/5/10/25 GbE
  - Wi-Fi 6E/7: 802.11ax/be, até 46 Gb/s teóricos
  
- **Áudio**: Codecs HD Audio, saídas digitais (S/PDIF, HDMI)

### Sistema de Energia e Refrigeração

#### **Fonte de Alimentação (PSU)**
- Eficiência: Certificação 80 Plus (Bronze, Silver, Gold, Platinum, Titanium)
- Potência: 450W a 1600W+
- Modularidade: Cabos destacáveis para melhor gerenciamento
- Rails: +12V principal para CPU/GPU

#### **Refrigeração**
- **Air Cooling**: Heat pipes, torres de alumínio/cobre, ventiladores PWM
- **Liquid Cooling**: AIO (All-in-One) 120mm-420mm, custom loops
- **Thermal Paste/Pad**: Interface térmica entre CPU/GPU e cooler

## Arquitetura de Von Neumann

A [arquitetura de Von Neumann](https://en.wikipedia.org/wiki/Von_Neumann_architecture) é um modelo de computador proposto por John von Neumann em 1945 no documento "First Draft of a Report on the EDVAC". Este modelo revolucionário estabeleceu os fundamentos da computação moderna e é baseado em princípios que permanecem relevantes quase 80 anos depois.

![arquitetura von neumann](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Von_Neumann_Architecture.svg/800px-Von_Neumann_Architecture.svg.png)

*Figura 5: Diagrama da arquitetura de Von Neumann mostrando o barramento único para dados e instruções.*

### Princípios Fundamentais

#### **1. Unidade de Processamento (CPU)**
A unidade de processamento é responsável por executar as instruções do programa, realizar operações aritméticas e lógicas, e controlar o fluxo de dados no computador. É composta por:

**ULA (Unidade Lógica e Aritmética / ALU):**
- Executa operações aritméticas (adição, subtração, multiplicação, divisão)
- Operações lógicas (AND, OR, XOR, NOT)
- Deslocamentos de bits e comparações
- Flags de status (zero, carry, overflow, sign)

**UC (Unidade de Controle / Control Unit):**
- Busca instruções da memória (fetch)
- Decodifica instruções (decode)
- Executa instruções (execute)
- Ciclo de instrução: Fetch-Decode-Execute-Writeback

**Registradores:**
- **PC (Program Counter)**: Endereço da próxima instrução
- **IR (Instruction Register)**: Instrução sendo executada
- **ACC (Accumulator)**: Resultados intermediários
- **SP (Stack Pointer)**: Topo da pilha
- **Registradores de propósito geral**: EAX, EBX, ECX, EDX (x86)

#### **2. Memória**
A memória é utilizada para armazenar dados e instruções do programa. Na arquitetura de Von Neumann, instruções e dados compartilham o mesmo espaço de endereçamento, diferentemente da arquitetura Harvard que os separa.

**Hierarquia de Memória:**

| Nível | Tipo | Velocidade | Capacidade | Volátil? |
|-------|------|------------|------------|----------|
| 0 | Registradores | <1 ns | KBs | Sim |
| 1 | Cache L1 | 1-3 ns | 32-128 KB | Sim |
| 2 | Cache L2 | 3-10 ns | 256 KB - 2 MB | Sim |
| 3 | Cache L3 | 10-30 ns | 2-128 MB | Sim |
| 4 | RAM Principal | 50-100 ns | 8-128 GB | Sim |
| 5 | SSD/NVMe | 10-100 μs | 256 GB - 8 TB | Não |
| 6 | HDD | 1-10 ms | 1-22 TB | Não |
| 7 | Fita/Cloud | 100ms - s | Ilimitado | Não |

**Memória Principal (RAM):**
- Armazenamento temporário de dados e instruções em execução
- Acesso aleatório (qualquer endereço em tempo constante)
- Volátil (perde dados sem energia)
- Endereçamento linear (barramento de endereços)

**Memória Secundária:**
- Armazenamento permanente (não-volátil)
- Maior capacidade, menor velocidade
- HDDs, SSDs, unidades ópticas, flash USB

#### **3. Unidade de Controle e Barramentos**
A unidade de controle coordena as operações do computador, controlando o fluxo de dados entre a unidade de processamento e a memória, e executando as instruções do programa através de barramentos:

**Barramento de Dados (Data Bus):**
- Transporta dados entre CPU, memória e I/O
- Largura: 64 bits em sistemas modernos
- Bidirecional

**Barramento de Endereços (Address Bus):**
- Especifica endereços de memória ou I/O
- Largura determina espaço endereçável (64 bits = 2^64 endereços teóricos)
- Unidirecional (CPU → memória)

**Barramento de Controle (Control Bus):**
- Sinais de controle (Read, Write, Interrupt, Clock, Reset)
- Coordena timing e operações
- Direção variável

### O "Gargalo de Von Neumann"

Uma limitação fundamental da arquitetura de Von Neumann é o **gargalo de Von Neumann**: como instruções e dados compartilham o mesmo barramento, a CPU não pode buscar uma instrução e ler/escrever dados simultaneamente. Isso limita o desempenho máximo do sistema.

**Soluções modernas:**
- **Caches hierárquicos**: Reduzem acessos à memória principal
- **Pipelining**: Execução sobreposta de múltiplas instruções
- **Superscalar**: Múltiplas unidades de execução paralelas
- **Previsão de desvio (branch prediction)**: Antecipa fluxos de controle
- **Memórias separadas para instruções/dados em caches L1** (arquitetura Harvard modificada)

### Arquiteturas Alternativas e Evoluções

#### **Arquitetura Harvard**
Separa fisicamente memórias e barramentos para instruções e dados, permitindo acesso simultâneo. Comum em:
- Microcontroladores (Arduino, PIC)
- DSPs (Digital Signal Processors)
- Caches L1 de CPUs modernas (Harvard modificada)

#### **Arquiteturas Paralelas e Distribuídas**
- **SIMD (Single Instruction, Multiple Data)**: GPUs, vetores
- **MIMD (Multiple Instruction, Multiple Data)**: Multicore, clusters
- **Computação Quântica**: Qubits, superposição, emaranhamento
- **Computação Neuromórfica**: Redes neurais em hardware (Intel Loihi, IBM TrueNorth)

## Exercícios

### Exercício 1: Identificação de Hardware

Descubra, usando ferramentas do Sistema operacional do seu computador, os seguintes parâmetros:

**Windows:**
```powershell
# Informações da CPU
wmic cpu get Name,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed,CurrentClockSpeed

# Memória RAM
wmic memorychip get Capacity,Speed,Manufacturer,PartNumber
systeminfo | findstr /C:"Total Physical Memory"

# Armazenamento
wmic diskdrive get Model,Size,InterfaceType
```

**Linux:**
```bash
# CPU
lscpu
cat /proc/cpuinfo
lshw -class cpu

# Memória
free -h
sudo dmidecode --type memory
cat /proc/meminfo

# Armazenamento
lsblk
sudo fdisk -l
df -h
```

**macOS:**
```bash
# CPU e Memória
sysctl -a | grep machdep.cpu
system_profiler SPHardwareDataType
system_profiler SPMemoryDataType

# Armazenamento
diskutil list
system_profiler SPStorageDataType
```

1. Qual o Modelo da CPU? (ex: Intel Core i7-12700K, AMD Ryzen 5 5600X, Apple M2)
2. Qual Clock da CPU? (frequência base e turbo em GHz)
3. Quantos Cores possui a sua CPU? (núcleos físicos e threads lógicos)
4. Qual O tamanho da memória RAM em Bytes e em GBytes?
5. Que tipo de unidade de Armazenamento de dados ele possui e qual a sua capacidade em GB? (SSD NVMe, SATA, HDD)

### Exercício 2: Mapeamento de I/O

Liste todos os tipos de I/O de que o seu computador é capaz:

**Categorias para identificar:**
- **Portas físicas**: USB (quantas? qual versão?), HDMI, DisplayPort, Thunderbolt, Ethernet (RJ45), áudio (3.5mm), leitor de cartões SD
- **Sem fio**: Wi-Fi (802.11 a/b/g/n/ac/ax/be?), Bluetooth (qual versão?), NFC
- **Legado**: PS/2, serial (DB9), paralela (DB25), VGA
- **Internos**: SATA ports, M.2 slots, PCIe slots (quantos? quais versões?)

**Comandos úteis:**
```bash
# Linux
lsusb           # Dispositivos USB
lspci           # Dispositivos PCIe
ip link         # Interfaces de rede
hwinfo --short  # Resumo completo

# Windows
deviceview      # Device Manager alternativo
Get-PnpDevice   # PowerShell
```

### Exercício 3: Upgrade e Expansibilidade

Que componentes do seu computador podem ser substituídos (melhorados)?

**Fatores a considerar:**
- **Socket da CPU**: É compatível com gerações mais novas? (ex: LGA1700, AM5)
- **Chipset**: Suporta CPUs mais potentes via BIOS update?
- **Slots de RAM**: Quantos slots livres? Qual velocidade máxima suportada?
- **PCIe**: Há slots livres para GPU, SSD NVMe, placas de rede?
- **PSU**: Potência suficiente para upgrades? Conectores disponíveis?
- **Gabinete**: Espaço físico para GPUs maiores, mais fans, radiadores?
- **Thermal**: Sistema de refrigeração adequado para CPUs mais quentes?

**Classifique:**
- ✅ Fácil upgrade (RAM, SSD, GPU)
- ⚠️ Upgrade moderado (CPU, cooler, PSU)
- ❌ Difícil/impossível (placa-mãe em laptops, componentes soldados)

### Exercício 4: Hardware Mobile

Quais componentes do seu computador você consegue identificar em seu telefone celular? Tente responder os itens do exercício 1 para o celular.

**Aplicativos de diagnóstico:**
- **Android**: CPU-Z, AIDA64, Device Info HW, Geekbench
- **iOS**: Lirum Device Info, CPU-x, Geekbench, 3DMark

**Componentes móveis equivalentes:**
| Desktop/Laptop | Smartphone |
|----------------|------------|
| CPU x86/ARM | SoC ARM (Snapdragon, Apple A-series, MediaTek) |
| GPU discreta | GPU integrada no SoC (Adreno, Mali, Apple GPU) |
| RAM DDR4/5 | LPDDR4X/LPDDR5 (Low Power) |
| SSD NVMe | UFS 3.1/4.0 ou eMMC |
| PCIe slots | Sem expansão (soldado) |
| PSU | Bateria Li-ion/Li-Po + PMIC |
| Cooling ativo | Passive cooling / vapor chamber |

**Diferenças arquiteturais:**
- **SoC (System on Chip)**: CPU, GPU, RAM, modem, ISP, DSP em um único die
- **Arquitetura ARM**: RISC vs x86 CISC
- **Eficiência energética**: Prioridade absoluta (TDP de 3-8W vs 65-250W)
- **Armazenamento**: Soldado, não substituível
- **RAM**: Soldada, sem upgrade

**Desafio adicional:**
Compare o desempenho relativo usando benchmarks:
- Geekbench 6 (single-core, multi-core)
- 3DMark Wild Life (GPU)
- AndroBench (storage speed)

Como o desempenho do seu smartphone se compara ao seu desktop/laptop? Em que tarefas o mobile é superior? Em que é inferior?

## Tópicos Avançados e Tendências

### Lei de Moore e Além

A **Lei de Moore** (observação de Gordon Moore em 1965) previu que o número de transistores em um chip dobraria aproximadamente a cada dois anos. Esta tendência se manteve por quase 50 anos, mas enfrenta limites físicos:

**Limites atuais:**
- Tamanho atômico (transistores de 3nm ≈ 15 átomos de silício)
- Dissipação de calor (densidade de potência)
- Efeitos quânticos (tunelamento em escalas nanométricas)
- Custo exponencial de fabs (TSMC 3nm: $20+ bilhões)

**Tecnologias emergentes:**
- **Chiplets**: Múltiplos dies interconectados (AMD Ryzen, Intel Meteor Lake)
- **3D stacking**: Empilhamento vertical de transistores (Intel Foveros, TSMC SoIC)
- **Novos materiais**: Grafeno, nanotubos de carbono, fósforo negro
- **Computação quântica**: Qubits supercondutores, íons aprisionados
- **Óptica integrada**: Fotônica em silício para interconexões

### Segurança em Hardware

**Vulnerabilidades modernas:**
- **Spectre/Meltdown** (2018): Exploração de execução especulativa
- **Rowhammer**: Ativação repetida de linhas de RAM para corromper células adjacentes
- **Side-channel attacks**: Análise de consumo de energia, tempo de execução, emissões eletromagnéticas

**Mitigações:**
- **TPM (Trusted Platform Module)**: Criptografia de chaves, atestação
- **Secure Boot**: Verificação criptográfica do bootloader
- **SGX/TrustZone**: Enclaves seguros de execução
- **Memory encryption**: AMD SEV, Intel TME

### Sustentabilidade e E-Waste

**Desafios ambientais:**
- **Consumo energético**: Data centers consomem ~1-2% da eletricidade global
- **E-waste**: 53.6 milhões de toneladas em 2019 (apenas 17.4% reciclados)
- **Materiais raros**: Ouro, prata, paládio, terras raras (disprósio, neodímio)

**Soluções:**
- **Right to Repair**: Legislação para reparabilidade
- **Modularidade**: Framework Laptop, Fairphone
- **Eficiência**: Arquiteturas ARM em servidores, accelerators especializados
- **Circular economy**: Reuso, refurbishment, reciclagem de metais preciosos

---

# Referências

## Livros e Artigos Acadêmicos

1. **Hennessy, J. L., & Patterson, D. A. (2014).** *Computer Architecture: A Quantitative Approach* (6th ed.). Morgan Kaufmann.  
   [https://www.elsevier.com/books/computer-architecture/hennessy/978-0-12-811905-1](https://www.elsevier.com/books/computer-architecture/hennessy/978-0-12-811905-1)  
   *Considerado a "bíblia" da arquitetura de computadores.*

2. **Patterson, D. A., & Hennessy, J. L. (2021).** *Computer Organization and Design RISC-V Edition* (2nd ed.). Morgan Kaufmann.  
   [https://www.elsevier.com/books/computer-organization-and-design-risc-v-edition/patterson/978-0-12-820331-6](https://www.elsevier.com/books/computer-organization-and-design-risc-v-edition/patterson/978-0-12-820331-6)

3. **Von Neumann, J. (1945).** *First Draft of a Report on the EDVAC.* Moore School of Electrical Engineering, University of Pennsylvania.  
   [https://www.virtualtravelog.net/wp/wp-content/media/2003/08/edvac.pdf](https://www.virtualtravelog.net/wp/wp-content/media/2003/08/edvac.pdf)  
   *Documento histórico fundacional.*

4. **Moore, G. E. (1965).** "Cramming more components onto integrated circuits." *Electronics*, 38(8), 114-117.  
   [https://doi.org/10.1109/N-SSC.2006.4785860](https://doi.org/10.1109/N-SSC.2006.4785860)  
   *Artigo original da Lei de Moore.*

5. **Kocher, P., et al. (2019).** "Spectre Attacks: Exploiting Speculative Execution." *Communications of the ACM*, 63(7), 93-101.  
   [https://doi.org/10.1145/3356900](https://doi.org/10.1145/3356900)

## Recursos Online e Tutoriais

6. **Dissecando o computador:**  
   [How does Computer Hardware Work?](https://youtu.be/d86ws7mQYIg)  
   *Visão geral dos componentes físicos.*

7. **Funcionamento da Memória RAM:**  
   [How does Computer Memory Work?](https://youtu.be/7J7X7aZvMXQ)  
   *Hierarquia de memória e funcionamento detalhado.*

8. **Funcionamento da CPU:**  
   [How does a CPU work?](https://youtu.be/42KTvGYQYn0)  
   *Arquitetura interna e ciclo de instrução.*

9. **AnandTech.** *CPU Architecture Deep Dives.*  
   [https://www.anandtech.com/tag/cpus](https://www.anandtech.com/tag/cpus)  
   *Análises técnicas detalhadas de processadores.*

10. **Tom's Hardware.** *PC Building Guide & Component Reviews.*  
    [https://www.tomshardware.com/reviews/best-cpus,3986.html](https://www.tomshardware.com/reviews/best-cpus,3986.html)

11. **Wikipedia.** *Von Neumann Architecture.*  
    [https://en.wikipedia.org/wiki/Von_Neumann_architecture](https://en.wikipedia.org/wiki/Von_Neumann_architecture)

12. **Wikipedia.** *Computer Hardware.**  
    [https://en.wikipedia.org/wiki/Computer_hardware](https://en.wikipedia.org/wiki/Computer_hardware)

## Especificações Técnicas

13. **Intel.** *Intel® 64 and IA-32 Architectures Software Developer's Manual.*  
    [https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)

14. **AMD.** *AMD64 Architecture Programmer's Manual.*  
    [https://www.amd.com/en/developer/amd64.html](https://www.amd.com/en/developer/amd64.html)

15. **JEDEC.** *DDR5 SDRAM Standard (JESD79-5).*  
    [https://www.jedec.org/standards-documents/docs/jesd79-5](https://www.jedec.org/standards-documents/docs/jesd79-5)

16. **PCI-SIG.** *PCI Express Base Specification.*  
    [https://pcisig.com/specifications](https://pcisig.com/specifications)

17. **NVM Express.** *NVMe Specification.*  
    [https://nvmexpress.org/specifications/](https://nvmexpress.org/specifications/)

## Vídeos Educacionais Avançados

18. **Branch Education.** *How do Transistors Work?*  
    [https://youtu.be/IcrBqCFLHIY](https://youtu.be/IcrBqCFLHIY)  
    *Animação 3D detalhada de semicondutores.*

19. **Ben Eater.** *Building an 8-bit computer from scratch.*  
    [https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE40pJHsUi5DK8ZJxdY](https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE40pJHsUi5DK8ZJxdY)  
    *Série completa sobre arquitetura de computadores.*

20. **Computerphile.** *Von Neumann Architecture.*  
    [https://youtu.be/7KA5nZLdK8E](https://youtu.be/7KA5nZLdK8E)

## Ferramentas de Diagnóstico

21. **CPUID.** *CPU-Z System Information.*  
    [https://www.cpuid.com/softwares/cpu-z.html](https://www.cpuid.com/softwares/cpu-z.html)

22. **HWiNFO.** *System Information & Diagnostic Tool.*  
    [https://www.hwinfo.com/](https://www.hwinfo.com/)

23. **Geekbench.** *Cross-Platform Benchmark.*  
    [https://www.geekbench.com/](https://www.geekbench.com/)

---

**Nota:** As figuras mencionadas neste texto são referências a imagens disponíveis publicamente. Para uso educacional, verifique sempre as licenças de uso (geralmente Creative Commons ou domínio público via Wikimedia Commons).

**Última atualização:** Fevereiro 2026
