from funcoes import *

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}     

for elem in frota.keys():
    if elem == 'porta-aviões':
        print(f'Insira as informações referentes ao navio {elem} que possui tamanho 4')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        orientação = int(input('[1] Vertical [2] Horizontal >'))
    elif elem == 'navio-tanque':
        for e in range(2):
            print(f'Insira as informações referentes ao navio {elem} que possui tamanho 3')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            orientação = int(input('[1] Vertical [2] Horizontal >'))
            if posicao_valida(frota, linha, coluna, orientação, 4):
                print('sla')

    elif elem == 'contratorpedeiro':
        for e in range(3):
            print(f'Insira as informações referentes ao navio {elem} que possui tamanho 2')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            orientação = int(input('[1] Vertical [2] Horizontal >'))
    elif elem == 'submarino':
        for e in range(4):
            print(f'Insira as informações referentes ao navio {elem} que possui tamanho 1')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
        orientação = 1
