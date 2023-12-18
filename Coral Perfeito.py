import os, sys, io

input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto, end="\n"):
    sys.stdout.write(str(texto) + end)

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
            imprimir(valor + 1)
        else:
            imprimir('-1')
    except EOFError:
        break
