# Exercício 1:

def define_posicoes(i, j, o, t):
    lista = []
    if o == "vertical":
        for k in range(t):
            lista.append([i + k, j])    
    elif o == "horizontal":
        for k in range(t):
            lista.append([i, j + k])    
    return lista

# Exercício 2:

def preenche_frota(frota, nv, i, j, o, t):
    posicoes = define_posicoes(i, j, o, t)

    if nv in frota:
        frota[nv].append(posicoes)
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

# Exercício 5:

def afundados(dicio , tab):
    cont = 0 
    for lista in dicio.values():
        for l in lista:
            t = len(l)
            c = 0
            for i,j in l:
                if tab[i][j] == 'X':
                    c += 1
            if c == t:
                cont += 1
    return cont

# Exercício 6:

def posicao_valida(dicio , i , j , o , t):
    lista = []
    if o == "vertical":
        for k in range(t):
            lista.append([i + k, j])    
    elif o == "horizontal":
        for k in range(t):
            lista.append([i, j + k])

    for i, j in lista:
        if i<0 or j<0 or i>9 or j>9:
            return False    
      
    for listas in dicio.values():
        for p in listas:
            for [linha, coluna] in p:
                if [linha, coluna] in lista:
                    return False
    return True


    
