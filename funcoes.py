def faz_jogada(tab, i, j):
    if tab[i][j] == 1:
        tab[i][j] = 'X'
    elif tab[i][j] == 0:
        tab[i][j] = '-'
    return tab