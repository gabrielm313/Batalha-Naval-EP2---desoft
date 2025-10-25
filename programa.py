from funcoes import *

tamanho = {
    "porta-aviões":4,
    "navio-tanque":3,
    "contratorpedeiro":2,
    "submarino": 1,
}     

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}     

for nome , t in tamanho.items():
    for i in range(t):
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