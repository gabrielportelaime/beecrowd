tamanho_fase = int(input())

caminhos = []

caminhos.append([int(x) for x in input().split()])
caminhos.append([int(x) for x in input().split()])

trocas = []

for j in range(2):
    if(caminhos[j][0] == 0):
        trocas.append(9999999)
    else:
        troca = 0
        valor = j
        i = 0
        while(i < tamanho_fase - 1):
            if(caminhos[valor][i] < caminhos[valor][i+1] or caminhos[valor][i+1] == 0):
                i -= 1
                troca += 1
                if(valor == 0):
                    valor = 1
                else:
                    valor = 0
            i += 1
        trocas.append(troca)

print(min(trocas))