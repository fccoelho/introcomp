val = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}
def soma_janelas(nrl):
    i = 0
    f = 2
    if len(set(nrl)) > 1:
        ls = []
        while True:
            if i > len(nrl)-1:
                break
            if len(set(nrl[i:i+3])) == 1:
                ls.append(sum(nrl[i:i+3]))
                i += 3
            elif len(set(nrl[i:i+2])) == 1:
                ls.append(sum(nrl[i:i + 2]))
                i += 2
            else:
                ls.append(nrl[i])
                i += 1

    return sum(ls)

def converte_romanos(nr):
    nr = nr.upper()
    nrl = [val[i] for i in nr]
    if set(nrl) == {1}:
        return sum(nrl)

    elif 'V' in nr:
        if nr.startswith("V"):
            return 4 + len(nr)
        elif nr.endswith("V"):
            if 'X' in nr:
                if 'I' in nr:
                    return 14
                return 15
            return 6 - len(nr)

    elif 'X' in nr:
        if nr.startswith("X"):
            return 9 + len(nr)
        elif nr.endswith("X"):
            return 11 - len(nr)
