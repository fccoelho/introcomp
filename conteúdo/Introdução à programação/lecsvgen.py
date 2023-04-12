

def gen_linha(nome_arq):
    with open(nome_arq,'r') as f:
        for i,l in enumerate(f.readlines()):
            if i >=4:
                yield l.strip().split('","') 
        
            
            
            
    # print(linhas[:2])
    # lcab = len(linhas[0])
    # for n, l in enumerate(linhas):
    #     try:
    #         assert len(l) == lcab
    #     except AssertionError:
    #         print (n, len(l))
        # print (l) 


if __name__=="__main__":
    nome_arq="dados.csv"
    # print(dir(parser.parse_args()))
    for l in gen_linha(nome_arq):
        print(l)
    # le_arquivo()
