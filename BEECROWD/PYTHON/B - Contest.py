for i in range(int(input())):
    m, ataque = [int(x) for x in input().split()]
    monstros = [int(x) for x in input().split()]
    espelho = []
    for j in range(len(monstros)):
        if(monstros[j]%ataque == 0):
            print(j+1, end=" ")
        else:
            espelho.append((monstros[j]%ataque, j + 1))
    monstros_ordenados = sorted(espelho, key=lambda monstro:monstro[0], reverse=True)
    for j in range(len(monstros_ordenados)):
        print(monstros_ordenados[j][1], end=" ")
    print("")