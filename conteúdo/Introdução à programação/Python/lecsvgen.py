def gen_linha(nome_arq):
    with open(nome_arq, 'r') as f:
        for i, l in enumerate(f.readlines()):
            if i >= 4:
                yield l.strip().strip('"').split('","')


def converte_linha(nome_arq):

    for linha in gen_linha(nome_arq):
        linha_convertida = []
        for el in linha:
            try:
                f = float(el)
                if int(f) == f:
                    linha_convertida.append(int(f))
                else:
                    linha_convertida.append(f)
            except ValueError:
                linha_convertida.append(el)
        yield linha_convertida



if __name__ == "__main__":
    nome_arq = "dados.csv"
    for l in converte_linha(nome_arq):
        print(l)
