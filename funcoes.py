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
    po = define_posicoes(i, j, o, t)
      
    for listas in dicio.values():
        for p in listas:
            for a,b in p:
                if [a,b] in po:
                    return False
    return True

frota = {
    "navio-tanque":[
      [[6,1],[6,2],[6,3]],
      [[4,7],[5,7],[6,7]]
    ],
    "contratorpedeiro":[
      [[1,1],[2,1]],
      [[2,3],[3,3]],
      [[9,1],[9,2]]
    ],
    "submarino": [
      [[0,3]],
      [[4,5]],
      [[8,9]],
      [[8,4]]
    ],
}
linha = 6
coluna = 2
orientacao = 'horizontal'
tamanho = 4
resultado = posicao_valida(frota, linha, coluna, orientacao, tamanho)
print(resultado)

    
