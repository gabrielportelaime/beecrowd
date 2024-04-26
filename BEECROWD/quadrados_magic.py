matriz = []
n = 4
for i in range(n):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)
valor = sum(linha)
acabou = False
for i in range(n):
    soma_linha = soma_coluna = 0
    for j in range(n):
        soma_linha += matriz[i][j]
        soma_coluna += matriz[j][i]
    if(soma_linha != valor or soma_coluna != valor):
        print('not magic')
        acabou = True
        break
if(not acabou):
    print('magic')
