matriz = []
n = int(input())
for i in range(n):
    linha = [int(x) for x in input().split()]
    matriz.append(linha) 
valor = sum(linha)
soma_principal = soma_secundaria = 0
acabou = False
for i in range(n):
    soma_linha = soma_coluna = 0
    for j in range(n):
        soma_linha += matriz[i][j]
        soma_coluna += matriz[j][i]
        if(i == j):
            soma_principal += matriz[i][j]
        if(i + j == n - 1):
            soma_secundaria += matriz[i][j]
    if(soma_linha != valor or soma_coluna != valor):
        print('0')
        acabou = True
        break
if(not acabou):
    if(soma_secundaria == valor and soma_principal == valor):
        print(valor)
    else:
        print('0')