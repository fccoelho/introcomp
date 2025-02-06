val = {"I": 1,
       "V": 5,
       "X": 10,
       "L": 50,
       "C": 100,
       "D": 500,
       "M": 1000}


def soma_iguais(nrl):
    i = 0
    if len(set(nrl)) > 1:
        ls = []
        while True:
            if i > len(nrl) - 1:
                break
            if len(set(nrl[i:i + 3])) == 1:
                ls.append(sum(nrl[i:i + 3]))
                i += 3
            elif len(set(nrl[i:i + 2])) == 1:
                ls.append(sum(nrl[i:i + 2]))
                i += 2
            else:
                ls.append(nrl[i])
                i += 1
    else:
        ls = nrl

    return ls


def soma_final(nrl):
    i = len(nrl) - 1
    nar = 0
    while i > 0:
        if nrl[i] > nrl[i - 1]:
            nar += (nrl[i] - nrl[i - 1])
            i -= 2
        else:
            nar += nrl[i]
            i -= 1
    return nar + nrl[0] if i == 0 else nar


def converte_romanos(nr):
    nr = nr.upper()
    nrl = [val[i] for i in nr]
    if set(nrl) == {1}:
        return sum(nrl)
    else:
        nrls = soma_iguais(nrl)
        return soma_final(nrls)
