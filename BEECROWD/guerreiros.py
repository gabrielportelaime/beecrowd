import os, sys, io

input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto, end="\n"):
    sys.stdout.write(str(texto) + end)

for i in range(int(input())):
    valor = int(input())
    raiz = (1 + 8*valor)**(1/2)
    resultado = (raiz - 1)/2
    print(int(resultado))