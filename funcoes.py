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
        frota[nv] = [posicoes]
    else:
        frota[nv] = [posicoes]

    return frota
    
# Exercício 3:

def faz_jogada(tab, i, j):
    if tab[i][j] == 1:
        tab[i][j] = 'X'
    elif tab[i][j] == 0:
        tab[i][j] = '-'
    return tab

# Exercício 4:

def posiciona_frota(dicio):
    tab = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tab.append(linha)
    
    for lista in dicio.values():
        for l in lista:
            for i,j in l:
                tab[i][j] = 1
    return tab


    
