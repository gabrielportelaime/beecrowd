for i in range(int(input())):
    input()
    lista = [int(x) for x in input().split()]
    ordenada = lista[:]
    ordenada.sort()
    sim = True
    for j in range(len(lista)):
        if(lista[j]%2 != ordenada[j]%2):
            print("NO")
            sim = False
            break
    if(sim):
        print("YES")