from funcoes import *

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

# tamanhos e quantidades esperadas
tamanho = {
    "porta-aviões": 4,
    "navio-tanque": 3,
    "contratorpedeiro": 2,
    "submarino": 1,
}

quantidade = {
    "porta-aviões": 1,
    "navio-tanque": 2,
    "contratorpedeiro": 3,
    "submarino": 4,
}

for nome in frota.keys():
    t = tamanho[nome]
    q = quantidade[nome]

    for u in range(q):
        colocado = False
        while not colocado:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {t}")
            i = int(input("Linha: "))
            j = int(input("Coluna: "))

            # orientacao: use strings 'vertical'/'horizontal' (como suas funções definem)
            if nome == "submarino":
                o = "vertical"   # padrão para tamanho 1 (não afeta o resultado)
            else:
                o_num = int(input("[1] Vertical [2] Horizontal >"))
                if o_num == 1:
                    o = "vertical"
                else:
                    o = "horizontal"

            # verifica posição (posicao_valida espera (frota, i, j, o, t))
            if not posicao_valida(frota, i, j, o, t):
                # mensagem EXATA pedida pelo enunciado
                print("Esta posição não está válida!")
            else:
                # preenche_frota tem assinatura que você usou: (frota, nv, i, j, o, t)
                frota = preenche_frota(frota, nome, i, j, o, t)
                colocado = True

print(frota)
