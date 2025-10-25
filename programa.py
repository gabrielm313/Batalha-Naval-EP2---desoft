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
            l = int(input("coloque a linha:"))
            c = int(input("coloque a coluna:"))

            if nome != "submarino":
                o = int(input("coloque a orientação:"))
                if o == 1:
                    o = 'vertical'
                elif o == 2:
                    o = 'horizontal'

            if posicao_valida(frota, l, c, o, t) == False:
                print("Esta posição não está válida!")
            else:
                define_posicoes(l, c, o, t)
                frota = preenche_frota(frota, nome, l, c, o, t)
                f = True

print(frota)