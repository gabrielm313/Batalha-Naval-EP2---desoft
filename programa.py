from funcoes import *

# Exercício 7:

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
            i = int(input("Linha:"))
            j = int(input("Coluna:"))

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

# Exercício 8:

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

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

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
        print("Posição já informada anteriormente!")
        continue

    opo = faz_jogada(opo , i , j)
    na = afundados(frota_opo , opo)

    if opo[i][j] == 'X':
        print("Você acertou um navio!")
    else:
        print("Você errou")

    if na == tn:
        print("Parabéns! Você afundou todos os navios do oponente!")
        jogando = False