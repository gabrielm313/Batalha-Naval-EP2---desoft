def posicao_valida(dicio , i , j , o , t):
    lista = []
    if o == "vertical":
        for k in range(t):
            lista.append([i + k, j])    
    elif o == "horizontal":
        for k in range(t):
            lista.append([i, j + k])  
    for listas in dicio.values():        # listas = lista de navios daquele tipo
        for navio in listas:             # navio = lista de posições (cada pos é lista/tuple)
            for pos in navio:
                # pos pode ser [i,j] ou (i,j). Desempacotamos.
                ni, nj = pos
                if (ni, nj) in lista:
                    return False

    # passou em todas as verificações
    return True