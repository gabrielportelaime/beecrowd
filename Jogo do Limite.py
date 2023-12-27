import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

quantidade, carta, limite = [int(x) for x in input().split()]

a = b = 0

for i in range(quantidade - 1):
    pilha = int(input())
    diferenca = abs(pilha - carta)
    if(diferenca <= limite):
        if(i%2 == 0 and diferenca <= limite):
            a += diferenca
        else:
            b += diferenca
        carta = pilha

imprimir(str(a) + " " + str(b))