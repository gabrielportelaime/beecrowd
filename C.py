for i in range(int(input())):
    input()
    pedidos = [int(x) for x in input().split()]
    pedidos.sort()
    soma = 0
    quantidade = 0
    for pedido in pedidos:
        if(soma < pedido):
            soma += pedido
            quantidade += 1
    print(quantidade, soma)