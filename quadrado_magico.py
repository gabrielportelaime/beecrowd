matriz = []
n = int(input())
valores = [0]*(1000005)
deu_ruim = False
for i in range(n):
    linha = [int(x) for x in input().split()]
    for numero in linha:
        if(numero > 1000000 or numero < 1):
            deu_ruim = True
            break
        else:
            valores[numero] = 1
    matriz.append(linha)
if(deu_ruim or sum(valores[1:n*n+1]) != n*n):
    print('0')
else:  
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