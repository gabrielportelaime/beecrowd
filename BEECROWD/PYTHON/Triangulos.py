import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

while(True):
    try:
        quantidade_arcos = int(input())
        arcos = [int(x) for x in input().split()]
        resposta = 0
        soma = 0
        for i in range(quantidade_arcos):
            soma += arcos[i]
        if(soma%3 != 0):
            imprimir('0')
        else:
            valor = soma//3
            for i in range(quantidade_arcos):
                soma = 0
                j = 0
                while(soma < valor):
                    indice = (i + j)%quantidade_arcos
                    soma += arcos[indice]
                    if(soma == valor):
                        resposta += 1
                        break
                    j += 1
        imprimir(str(resposta//3))
    except EOFError:
        break
