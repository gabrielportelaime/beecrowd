for _ in range(int(input())):
    linhas, colunas = [int(x) for x in input().split()]
    matriz = []
    contadores = []
    for i in range(linhas):
        linha = list(input())
        matriz.append(linha)
        contadores.append([0]*colunas)
    for i in range(linhas):
        for j in range(colunas):
            if(matriz[i][j] == '@'):
                for k in range(i+1, linhas):
                    if(matriz[k][j] != '#'):
                        contadores[k][j] += 1
                    else:
                        break
                for k in range(i-1, -1, -1):
                    if(matriz[k][j] != '#'):
                        contadores[k][j] += 1
                    else:
                        break
                for k in range(j+1, colunas):
                    if(matriz[i][k] != '#'):
                        contadores[i][k] += 1
                    else:
                        break
                for k in range(j-1, -1, -1):
                    if(matriz[i][k] != '#'):
                        contadores[i][k] += 1
                    else:
                        break 
    maximo = 0
    for i in range(linhas):
        for j in range(colunas):
            if(contadores[i][j] > maximo):
                maximo = contadores[i][j]
                linha = i
                coluna = j
    print(str(linha) + ", " + str(coluna))