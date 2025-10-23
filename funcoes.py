# Exercício 1:


def define_posicoes(i , j , o , t):
    lista = []
    if o == "vertical":
        for k in range(t):
            lista.append((i + k, j)) #posições na vertical
    elif o == "horizontal":
        for k in range(t):
            lista.append([i , j + k]) #posições na horizontal
    return lista

def preenche_frota(frota, nv , i, j, o, t):
    posicoes = define_posicoes(i, j, o, t) 

    dicio = {}

    for navio in frota:
        if navio == nv:
            dicio[navio] = posicoes

    return frota

print(preenche_frota({'porta-aviões': [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]], 'navio-tanque': [[(2, 2), (3, 2), (4, 2), (5, 2)]], 'contratorpedeiro': [[(9, 0), (9, 1), (9, 2)]], 'submarino': [[(4, 5), (4, 6)]]}, 'submarino', 6, 0, 'horizontal', 2))