'''
https://code-with-me.global.jetbrains.com/jHijHdtv71P8UUyG-748bQ#p=PC&fp=695EB8B2B16D8C3DBFCBDAF1FD27AFFDBC7554A5160BE613A9AA14E22EAF0916&newUi=true
'''
import random
from collections import defaultdict
import time

LOTACAO = 8
ANDARES = 14
POPULAÇÃO = defaultdict(lambda :0)
FILAS_DE_ANDAR = defaultdict(lambda : 0)
DESEMBARCADOS = 0
EMBARCADOS = 0
CICLOS = 0

## variáveis de estado
ci_elv = [('andar_ant',0),('andar', 0), ('npass', 0), ('passageiros',[]), ('direção', 0), ('chamadas', [])]
ci_sim = [('fila', 0), ('energia', 0.0), ('viagens', 0)]


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
            if sim['fila'] == 0:
                break
            EMBARCADOS += 1
        else:
            if FILAS_DE_ANDAR[andar] == 0:
                return
            elv['passageiros'].append(0)
            FILAS_DE_ANDAR[andar] -= 1
        npass += 1
        elv['npass'] = npass


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
    for i,p in enumerate(elevador['passageiros']):
        if p == andar:
            elevador['passageiros'].pop(i)
            DESEMBARCADOS += 1
        if andar != 0:
            POPULAÇÃO[andar] += 1

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
    estado_e1 = dict(ci_elv)
    estado_e2 = dict(ci_elv)
    # simulação
    estado_sim = dict(ci_sim)
    for i in range(1,ANDARES+1):
        POPULAÇÃO[i]
    return (estado_e1,estado_e2),estado_sim

def gera_fila():
    n = random.randint(1,3)
    sim['fila'] += n


def atualiza_chamadas(andar=0):
    """
    Adiciona destinos aos elevadores
    :param andar:
    """
    if andar not in elevadores[0]['chamadas']:
        elevadores[0]['chamadas'].append(andar)
    if andar not in elevadores[1]['chamadas']:
        elevadores[1]['chamadas'].append(andar)


def move(elv):
    """
    Determina destino do elevador
    :param elv: Elevador
    """
    if not elv['chamadas']:
        return
    distancias = [abs(elv['andar']- c) for c in elv['chamadas']]
    destino = elv['chamadas'][distancias.index(min(distancias))]
    elv['direção'] = 1 if destino > elv['andar'] else -1
    elv['andar_ant'] = elv['andar']
    elv['andar'] = destino


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
    while True:
        gera_fila()
        operação()
        saidas()
        if i>n:
            break
        CICLOS += 1
        i += 1
        print(f"{i}:Tamanho da fila: {sim['fila']}; Embarcados: {EMBARCADOS}; Desembarcados: {DESEMBARCADOS}\r",end="")



if __name__ == "__main__":
    elevadores, sim = init_sim()
    loop_de_evento(100)