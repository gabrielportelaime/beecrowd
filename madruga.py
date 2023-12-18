while(True):
    quantidade, area = [int(x) for x in input().split()]
    if(quantidade == area == 0):
        break
    tiras = [int(x) for x in input().split()]
    soma = sum(tiras)
    if(soma == area):
        print(":D")
    else:
        maximo = max(tiras)
        