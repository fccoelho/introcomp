import sys

def le_arquivo(nome_arq):
    with open(nome_arq,'r') as f:
        linhas = [tuple(l.strip().split('","')) \
                  for l in f.readlines()[4:]]
    # print(linhas[:2])
    lcab = len(linhas[0])
    for n, l in enumerate(linhas):
        try:
            assert len(l) == lcab
        except AssertionError:
            print (n, len(l))
        # print (l) 


if __name__=="__main__":
    le_arquivo(nome_arq=sys.argv[1])