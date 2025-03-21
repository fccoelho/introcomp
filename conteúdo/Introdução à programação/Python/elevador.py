'''
https://code-with-me.global.jetbrains.com/jHijHdtv71P8UUyG-748bQ#p=PC&fp=695EB8B2B16D8C3DBFCBDAF1FD27AFFDBC7554A5160BE613A9AA14E22EAF0916&newUi=true
'''
import random
from collections import defaultdict
import time
from matplotlib import pyplot as plt

LOTACAO = 8
ANDARES = 14
POPULAÇÃO = defaultdict(lambda :0)
FILAS_DE_ANDAR = defaultdict(lambda : 0)
DESEMBARCADOS = 0 # Numero de pessoas entregues em andares != térreo
EMBARCADOS = 0 # numero total de pessoas que pegaram elevadores durante a simulação
CICLOS = 0
ANDARES_PERCORRIDOS = 0




## API do elevador
def embarque(elv=0):
    """
    Realiza o embarque no andar
    :param elv: id do elevador
    """
    global EMBARCADOS
    npass = elv['npass']
    andar = elv['andar']
    while (npass < LOTACAO):
        if andar == 0:
            if sim['fila'] == 0:
                return
            destino = escolhe_destino()
            elv['passageiros'].append(destino)
            if destino not in elv['chamadas']:
                elv['chamadas'].append(destino)
            sim['fila'] -= 1
            EMBARCADOS += 1
            elv['npass'] = len(elv['passageiros'])
            if sim['fila'] == 0:
                break
        else:
            if FILAS_DE_ANDAR[andar] == 0:
                return
            elv['passageiros'].append(0)
            FILAS_DE_ANDAR[andar] -= 1
            elv['npass'] = len(elv['passageiros'])
        npass += 1



def escolhe_destino():
    return random.randint(1, ANDARES)
def operação():
    '''
    Define as ações do elevador em função dos estados da simulação e dos elevadores
    '''
    for elv in elevadores:
        desembarque(elv)
        embarque(elv)
        move(elv)

def desembarque(elevador):
    """
    Realiza o desembarque de passageiros no andar
    :param andar: andar do desmbarque
    """
    global DESEMBARCADOS
    andar = elevador['andar']
    pass_saindo = elevador['passageiros'].count(andar)
    if pass_saindo > 0:
        for i in range(pass_saindo):
            elevador['passageiros'].remove(andar)
            if andar != 0:
                POPULAÇÃO[andar] += 1
                DESEMBARCADOS += 1 # não conto desembarques no térreo

    elevador['npass'] = len(elevador['passageiros'])

def chamada(n):
    """
    atualiza estado em resposta a uma chamada no andar n
    :param n: andar em que foi chamado o elevador
    """
    pass

def input_int(n):
    pass
## Eventos
eventos ={
    'embarque': embarque,
    'chamada' : chamada,
    'input_int': input_int,
    'desembarque': desembarque
}

def init_sim():
    ## Elevadores
    estado_e1 = dict([('andar_ant',0),('andar', 0), ('npass', 0), ('passageiros',[]), ('direção', 0), ('chamadas', [])])
    estado_e2 = dict([('andar_ant',0),('andar', 0), ('npass', 0), ('passageiros',[]), ('direção', 0), ('chamadas', [])])
    # simulação
    estado_sim = dict([('fila', 0), ('energia', 0.0), ('viagens', 0)])
    for i in range(1,ANDARES+1):
        POPULAÇÃO[i]
    return (estado_e1,estado_e2),estado_sim

def gera_fila():
    n = random.randint(1,3)
    sim['fila'] += n

def gera_fila_bench(i):
    fila = [2, 2, 1, 1, 3, 1, 2, 2, 3, 2, 1, 1, 2, 3, 1, 1, 3, 2, 3, 3, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 3, 1,
            1, 1, 1, 3, 2, 1, 2, 1, 3, 3, 1, 3, 3, 1, 2, 3, 2, 2, 3, 1, 2, 3, 1, 3, 2, 2, 1, 3, 2, 3, 2, 1, 1,
            1, 2, 2, 3, 1, 1, 1, 3, 3, 2, 1, 1, 3, 3, 2, 3, 3, 1, 1, 3, 2, 3, 3, 1, 1, 1, 2, 2, 3, 1, 2, 3, 2, 1, 3]
    # print(i)
    sim['fila'] += fila[i]
def atualiza_chamadas(andar=0):
    """
    Adiciona destinos aos elevadores
    :param andar:
    """
    for elv in elevadores:
        if elv['andar'] == andar:
            continue
        if andar not in elv['chamadas']:
            elv['chamadas'].append(andar)


def move(elv):
    """
    Determina destino do elevador
    :param elv: Elevador
    """
    global ANDARES_PERCORRIDOS
    if not elv['chamadas']:
        return
    distancias = [abs(elv['andar']- c) for c in elv['chamadas']]
    destino = elv['chamadas'][distancias.index(min(distancias))]
    elv['direção'] = 1 if destino > elv['andar'] else -1
    elv['andar_ant'] = elv['andar']
    elv['andar'] = destino
    elv['chamadas'].remove(destino)
    ANDARES_PERCORRIDOS += abs(elv['andar'] - elv['andar_ant'])


def saidas():
    """
    Gera filas de saída nos andares
    """
    andar = random.randint(1, ANDARES)  # Sorteia um andar
    descendo = random.randint(0,POPULAÇÃO[andar]) # determina quantos passageiros
    FILAS_DE_ANDAR[andar] += descendo # Atualiza fila
    atualiza_chamadas(andar)


def loop_de_evento(n):
    global CICLOS
    i=0
    entregas = []
    while True:
        # gera_fila()
        gera_fila_bench(i)
        operação()
        saidas()
        if sim['fila'] > 0:
            atualiza_chamadas(0) # Chama os elevadores para o andar 0 caso tenha fila
        if i == n:
            break
        CICLOS += 1
        i += 1
        entregas.append(DESEMBARCADOS)
        if i < n:
            print(f"{i}:Tamanho da fila: {sim['fila']}; Embarcados: {EMBARCADOS}; Desembarcados: {DESEMBARCADOS}; Andares Percorridos: {ANDARES_PERCORRIDOS}\r",end="" )
        else:
            eficiência = DESEMBARCADOS / ANDARES_PERCORRIDOS
            print(f"{i}:Tamanho da fila: {sim['fila']}; Embarcados: {EMBARCADOS}; Desembarcados: {DESEMBARCADOS}; Andares Percorridos: {ANDARES_PERCORRIDOS}; Eficiência: {eficiência}")

    return entregas, eficiência


if __name__ == "__main__":
    elevadores, sim = init_sim()
    entregas=[]
    eficiências=[]
    n = 100
    loop_de_evento(n)
    # for i in range(100):
    #     en,ef = loop_de_evento(100)
    #     entregas.append(en)
    #     eficiências.append(ef)
    #     DESEMBARCADOS = 0  # Numero de pessoas entregues em andares != térreo
    #     EMBARCADOS = 0  # numero total de pessoas que pegaram elevadores durante a simulação
    #     CICLOS = 0
    #     ANDARES_PERCORRIDOS = 0
    #
    # print(elevadores)
    # plt.plot(entregas)
    # plt.title("Passageiros Entregues a cada ciclo")
    # plt.xlabel("ciclos")
    # plt.figure()
    # plt.hist(eficiências)
    # plt.xlabel("Eficiência")
    # plt.show()
