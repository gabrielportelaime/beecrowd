while(True):
    n, m = [int(x) for x in input().split()]
    if(n == m == 0):
        break
    vazio = 'X'*(m+2)
    matriz = []
    matriz.append(list(vazio))
    fila = []
    for i in range(n):
        linha = list('X'+input()+'X')
        matriz.append(linha)
        for j in range(m):
            if(matriz[i+1][j+1] == 'T'):
                fila.append((i+1, j+1))
    matriz.append(list(vazio))
    while(len(fila) > 0):
        i, j = fila[0][0], fila[0][1]
        fila.pop(0)
        if(matriz[i-1][j] == 'A'):
            matriz[i-1][j] = 'T'
            fila.append((i-1, j))
        if(matriz[i][j-1] == 'A'):
            matriz[i][j-1] = 'T'
            fila.append((i, j-1))
        if(matriz[i+1][j] == 'A'):
            matriz[i+1][j] = 'T'
            fila.append((i+1, j))
        if(matriz[i][j+1] == 'A'):
            matriz[i][j+1] = 'T'
            fila.append((i, j+1))
    for i in range(1, n + 1):
        linha = matriz[i]
        linha.pop(0)
        linha.pop(-1)
        print(''.join(linha))
    print("")
