'''
https://code-with-me.global.jetbrains.com/jHijHdtv71P8UUyG-748bQ#p=PC&fp=695EB8B2B16D8C3DBFCBDAF1FD27AFFDBC7554A5160BE613A9AA14E22EAF0916&newUi=true
'''
import random

LOTACAO = 8

## variáveis de estado
ci_elv = [('andar', 0), ('npass', 0), ('direção', 0), ('chamadas', [])]
ci_sim = [('fila', 0), ('energia', 0.0), ('viagens', 0)]

## API do elevador
def embarque(andar=0):
    pos_elv = [e['andar'] for e in elvs]
    if andar in pos_elv:
        elv_i = pos_elv.index(andar) # decobre qual elevador está no andar
        elv = elvs[elv_i]
        npass = elv['npass']
        while npass < LOTACAO:
            npass +=1
            sim['fila'] -= 1
            if sim['fila'] == 0:
                break
        elv['npass'] = npass


def desembarque(n):
    pass
def chamada(n):
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
    return (estado_e1,estado_e2),estado_sim

def gera_fila():
    n = random.randint(1,5)
    sim['fila'].append(n)
    if 0 not in elvs[0]['chamadas']:
        elvs[0]['chamadas'].append(0)
    if 0 not in elvs[1]['chamadas']:
        elvs[1]['chamadas'].append(0)

def move(elv):
    pass

def loop_de_evento(n):
    i=0
    while True:
        gera_fila()
        if sim['fila']:
            eventos['embarque'](0)
        move()
        if i>n:
            break


if __name__ == "__main__":
    elvs, sim = init_sim()
    loop_de_evento(10)