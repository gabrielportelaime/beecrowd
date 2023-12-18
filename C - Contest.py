for i in range(int(input())):
    m, copias = [int(x) for x in input().split()]
    string = " " + input()
    conjunto = set()
    for j in range(copias):
        inicio, fim = [int(x) for x in input().split()]
        inicio1 = inicio
        fim1 = fim
        while(inicio1 <= fim and string[inicio1] != '1'):
            inicio1 += 1
        while(fim1 >= inicio and string[fim1] != '0'):
            fim1 -= 1   
        if(inicio1 > fim1):
            conjunto.add((-1, -1))
        else:
            conjunto.add((inicio1, fim1))
    print(len(conjunto))