# Exercício 1:


def define_posicoes(i , j , o , t):
    lista = []
    if o == "vertical":
        for k in range(t):
            lista.append((i + k, j)) #posições na vertical
    elif o == "horizontal":
        for k in range(t):
            lista.append((i , j + k)) #posições na horizontal
    return lista

def preenche_frota(frota, nv , i, j, o, t):
    posicoes = define_posicoes(i, j, o, t)

    if nv in frota:
        frota[nv].append(posicoes)
    else:
        frota[nv] = [posicoes]

    return frota
