import os, sys, io

input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto, end="\n"):
    sys.stdout.write(str(texto) + end)

quantidade = int(input())
lista = [int(x) for x in input().split()]
maximo = max(lista)

presenca = 1000005*[False]

for i in range(quantidade):
    presenca[lista[i]] = True

x = 1
resposta = 0
while(x <= maximo):
    y = x + 2 
    while(x*y <= maximo):
        aj = x*y
        ai = (y-x)//2 
        if(presenca[ai] and presenca[aj]):
            resposta += 1
        y += 2
    x += 1

imprimir(resposta)