'''
https://code-with-me.global.jetbrains.com/jHijHdtv71P8UUyG-748bQ#p=PC&fp=695EB8B2B16D8C3DBFCBDAF1FD27AFFDBC7554A5160BE613A9AA14E22EAF0916&newUi=true
'''
import random
from collections import defaultdict

LOTACAO = 8
ANDARES = 14
POPULAÇÃO = defaultdict(lambda :0)
FILAS_DE_ANDAR = defaultdict(lambda : 0)
DESEMBARCADOS = 0

## variáveis de estado
ci_elv = [('andar', 0), ('npass', 0), ('passageiros',[]), ('direção', 0), ('chamadas', [])]
ci_sim = [('fila', 0), ('energia', 0.0), ('viagens', 0)]


## API do elevador
def embarque(andar=0):
    """
    realiza o embarque no andar
    :param andar: Andar do embarque
    """
    pos_elv = [e['andar'] for e in elevadores]
    if andar in pos_elv:
        try:
            elv_i = pos_elv.index(andar) # descobre qual elevador está no andar
        except ValueError:
            return
        elv = elevadores[elv_i]
        npass = elv['npass']
        while npass < LOTACAO:
            npass +=1
            if andar == 0:
                elv['passageiros'].append(escolhe_destino())
                sim['fila'] -= 1
                if sim['fila'] == 0:
                    break
            else:
                elv['passageiros'].append(0)
                FILAS_DE_ANDAR[andar] -= 1
                if FILAS_DE_ANDAR[andar] == 0:
                    break

        elv['npass'] = npass


def escolhe_destino():
    return random.randint(1, ANDARES)
def operação():
    '''
    Define as ações do elevador em função dos estados da simulação e dos elevadores
    '''
    for elv in elevadores:
        embarque()
def desembarque(andar, elevador):
    """
    realiza o desembarque de passageiros no andar
    :param andar: andar do desmbarque
    """
    global DESEMBARCADOS
    for i,p in enumerate(elevador['passageiros']):
        if p == andar:
            elevador['passageiros'].pop(i)
        if andar != 0:
            POPULAÇÃO[andar] += 1
        DESEMBARCADOS += 1
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
    n = random.randint(1,5)
    sim['fila'] += n
    atualiza_chamadas()


def atualiza_chamadas(andar=0):
    if andar not in elevadores[0]['chamadas']:
        elevadores[0]['chamadas'].append(andar)
    if andar not in elevadores[1]['chamadas']:
        elevadores[1]['chamadas'].append(andar)


def move(elv):
    pass

def saidas():
    andar = random.randint(1, ANDARES)
    descendo = random.randint(0,POPULAÇÃO[andar])
    FILAS_DE_ANDAR[andar] += descendo
    atualiza_chamadas(andar)


def loop_de_evento(n):
    i=0
    while True:
        gera_fila()
        operação()
        saidas()
        if i>n:
            break


if __name__ == "__main__":
    elevadores, sim = init_sim()
    loop_de_evento(10)