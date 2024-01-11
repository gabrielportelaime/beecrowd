tamanho, quantidade = [int(x) for x in input().split()]
teste = 1
while(tamanho != 0 and quantidade != 0):
    sorveteiros = []
    for i in range(quantidade):
        inicio, fim = [int(x) for x in input().split()]
        sorveteiros.append((inicio, fim))
    sorveteiros.sort()
    inicio = sorveteiros[0][0]
    fim = sorveteiros[0][1]
    i = 1
    print("Teste", teste)
    teste += 1
    while(i < quantidade):
        while (i < quantidade and sorveteiros[i][0] <= fim):
            if (sorveteiros[i][1] > fim):
                fim = sorveteiros[i][1]
            i += 1  
        print(inicio, fim)
        if(i < quantidade):
            inicio = sorveteiros[i][0]
            fim = sorveteiros[i][1]
        i += 1
    if(i == quantidade):
        print(inicio, fim)
    print("")
    tamanho, quantidade = [int(x) for x in input().split()]