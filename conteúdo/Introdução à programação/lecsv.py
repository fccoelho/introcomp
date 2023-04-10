import argparse

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
    parser = argparse.ArgumentParser(description='Lê um arquivo CSV')
    parser.add_argument("csv", type=open, help="Arquivo CSV")
    # print(dir(parser.parse_args()))
    le_arquivo(nome_arq=parser.parse_args().csv.name)
