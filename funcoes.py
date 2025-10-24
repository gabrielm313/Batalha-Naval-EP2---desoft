# Exercício 1:

def define_posicoes(i, j, o, t):
    lista = []
    if o == "vertical":
        for k in range(t):
            lista.append([i + k, j])    # tupla (linha, coluna)
    elif o == "horizontal":
        for k in range(t):
            lista.append([i, j + k])    # tupla (linha, coluna)
    return lista

# Exercício 2:

def preenche_frota(frota, nv, i, j, o, t):
    posicoes = define_posicoes(i, j, o, t)

    if nv in frota:
        frota[nv].append(posicoes)
    else:
        frota[nv] = [posicoes]
    return frota

def faz_jogada(tab, i, j):
    for linha in range(len(tab)):
        if linha == i:
            for coluna in range(len(tab[linha])):
                if coluna == j:
                    if tab[linha][coluna] == 1:
                        tab[linha][coluna] = "X"
                    else:
                        tab[linha][coluna] = "-"
    return tab