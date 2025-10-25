from funcoes import *
frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

for nome in frota.keys():
    if nome == "porta-aviões":
        t = 4
        q = 1
    elif nome == "navio-tanque":
        t = 3
        q = 2
    elif nome == "contratorpedeiro":
        t = 2
        q = 3
    elif nome == "submarino":
        t = 1
        q = 4

    for v in range(q):
        f = False
        while not f:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {t}")
            i = int(input("linha:"))
            j = int(input("coluna:"))

            if nome != "submarino":
                o = int(input("orientação:"))
                if o == 1:
                    o = 'vertical'
                elif o == 2:
                    o = 'horizontal'

            if posicao_valida(frota, i, j, o, t) == False:
                print("Esta posição não está válida!")
            else:
                define_posicoes(i, j, o, t)
                frota = preenche_frota(frota, nome, i, j, o, t)
                f = True

frota_opo = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

opo = posiciona_frota(frota_opo)
jog = posicao_valida(frota)

jogando = True
tn = 10
na = 0

while jogando:
    print(monta_tabuleiros(jog, opo))

    i = int(input("Jogador, qual linha deseja atacar? "))
    if i < 0 or i > 9:
        print("Linha inválida!")
        continue

    j = int(input("Jogador, qual coluna deseja atacar? "))
    if j < 0 or j > 9:
        print("Coluna inválida!")
        continue

    if opo[i][j] == 'X' or opo[i][j] == '-':
        print("Posição já informadaanteriormente!")
        continue

    opo = faz_jogada(opo , i , j)
    na = afundados(frota_opo , opo)

    if opo[i][j] == 'X':
        print("Você acertou um navio!")
    else:
        print("Você errou")

    if na == tn:
        print("Parabéns! Você afundou todos os vavios do oponente!")
        jogando = False