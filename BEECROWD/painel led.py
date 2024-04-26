def trocas(estado, qtd_trocas):
    if(qtd_trocas == 0):
        return 0
    elif(estado == "X"):
        return qtd_trocas//2
    elif(qtd_trocas % 2 == 0):
        return qtd_trocas//2
    else:
        return qtd_trocas//2 + 1

def estado_final(estado, qtd_trocas):
    if(qtd_trocas%2 == 0):
        return estado
    elif(estado == "X"):
        return "O"
    else:
        return "X"

for i in range(int(input())):
    lampadas, vezes = input().split()
    lampadas = list(lampadas)
    vezes = int(vezes)
    for i in range(len(lampadas)):
        trocasprox = trocas(lampadas[i], vezes)
        lampadas[i] = estado_final(lampadas[i], vezes)
        vezes = trocasprox
    print(''.join(lampadas))

    