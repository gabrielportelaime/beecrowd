while(True):
    dic = {}
    n, m = [int(x) for x in input().split()]
    lista = [int(x) for x in input().split()]

    for i in range(n):
        numero = lista[i]
        if(numero not in dic):
            dic[numero] = [i]
        else:
            dic[numero].append(i)

    for i in range(m):
        ocorrencia, numero = [int(x) for x in input().split()]
        if((numero not in dic) or (ocorrencia > len(dic[numero]))):
            print("0")
        else:
            print(dic[numero][ocorrencia-1] + 1)