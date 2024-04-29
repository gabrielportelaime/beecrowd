while True:
    try:
        quantidade = int(input())
        lista = [int(x) for x in input().split()]
        soma = sum(lista)
        if(soma%quantidade == 0):
            valor = 0
            for i in range(quantidade):
                if(lista[i] > soma//quantidade):
                    valor += lista[i] - soma//quantidade
            print(valor + 1)
        else:
            print('-1')
    except EOFError:
        break
