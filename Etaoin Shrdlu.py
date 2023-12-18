import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto, end="\n"):
    sys.stdout.write(str(texto) + end)

linhas = int(input())

while(linhas != 0):
    texto = ""
    pares = {}
    for i in range(linhas):
        texto += input()
        for j in range(len(texto) - 1):
            if(texto[j] + texto[j + 1] not in pares):
                pares[texto[j] + texto[j + 1]] = 1
            else:
                pares[texto[j] + texto[j + 1]] += 1
    linhas = int(input())
    imprimir(pares)