from funcoes import *

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}     
for nome in frota.keys():
    if nome == "porta-aviões":
        t = 4
        q = 1
    elif nome == "navio-tanque":
        t = 3
        q = 2
    elif nome == "contratorpedeiro":
        t = 2
        q = 3
    elif nome == "submarino":
        t = 1
        q = 4

    for i in range(q):
        while True:
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho {t}')
            l = int(input('Linha: '))
            c = int(input('Coluna: '))
            if nome != 'submarino':
                o = int(input('[1] Vertical [2] Horizontal >'))
                if o == 1:
                    o = 'vertical'
                elif o == 2:
                    o = 'horizontal'
            if not posicao_valida(frota , l , c , o , t):
                print('Esta posição não está válida')
            else:
                define_posicoes( l , c , o , t)
                frota = preenche_frota(frota , nome , l , c , o , t)

print(frota)