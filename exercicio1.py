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