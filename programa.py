# Exercício 8
from funcoes import (
    posiciona_frota, faz_jogada, afundados,
    posicao_valida, monta_tabuleiros,
    define_posicoes, preenche_frota
)

import random
random.seed(2)

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

navios = {
    "porta-aviões": [4],
    "navio-tanque": [3, 3],
    "contratorpedeiro": [2, 2, 2],
    "submarino": [1, 1, 1, 1],
}

for tipo in navios:
    for tamanho in navios[tipo]:
        while True:
            print(f"Insira as informações referentes ao navio {tipo} que possui tamanho {tamanho}")
            try:
                l = int(input("Linha: "))
                c = int(input("Coluna: "))
            except ValueError:
                print("Entrada inválida! Digite números inteiros.")
                continue

            if tipo != 'submarino':
                try:
                    orientacao_in = int(input("[1] Vertical [2] Horizontal > "))
                except ValueError:
                    print("Entrada inválida! Digite 1 ou 2.")
                    continue
                if orientacao_in == 1:
                    orientacao = 'vertical'
                elif orientacao_in == 2:
                    orientacao = 'horizontal'
                else:
                    print("Orientação inválida! Digite 1 ou 2.")
                    continue
            else:
                orientacao = 'vertical'

            if posicao_valida(frota, l, c, orientacao, tamanho):
                frota = preenche_frota(frota, tipo, l, c, orientacao, tamanho)
                break
            else:
                print("Esta posição não está válida!")

frota_oponente = {
    'porta-aviões': [[[9, 1], [9, 2], [9, 3], [9, 4]]],
    'navio-tanque': [[[6, 0], [6, 1], [6, 2]], [[4, 3], [5, 3], [6, 3]]],
    'contratorpedeiro': [[[1, 6], [1, 7]], [[0, 5], [1, 5]], [[3, 6], [3, 7]]],
    'submarino': [[[2, 7]], [[0, 6]], [[9, 7]], [[7, 6]]]
}

opo = posiciona_frota(frota_oponente)
jog = posiciona_frota(frota)

print(monta_tabuleiros(jog, opo))

while True:
    try:
        l = int(input('Jogador, qual linha deseja atacar? '))
    except ValueError:
        print('Linha inválida!')
        continue
    if l < 0 or l > 9:
        print('Linha inválida!')
        continue

    try:
        c = int(input('Jogador, qual coluna deseja atacar? '))
    except ValueError:
        print('Coluna inválida!')
        continue
    if c < 0 or c > 9:
        print('Coluna inválida!')
        continue

    if opo[l][c] == '-' or opo[l][c] == 'X':
        print(f'A posição linha {l} e coluna {c} já foi informada anteriormente!')
        continue

    opo = faz_jogada(opo, l, c)

    if afundados(frota_oponente, opo) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        break

    while True:
        lo = random.randint(0, 9)
        co = random.randint(0, 9)
        if jog[lo][co] == '-' or jog[lo][co] == 'X':
            continue
        jog = faz_jogada(jog, lo, co)
        print(f"Seu oponente está atacando na linha {lo} e coluna {co}")
        break

    if afundados(frota, jog) == 10:
        print("O oponente derrubou toda a sua frota")
        break

    print(monta_tabuleiros(jog, opo))
