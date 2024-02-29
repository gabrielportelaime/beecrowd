
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

dicionario = {}
limite = 200001
soma = 0
for i in range(limite):
    soma += sum([int(x) for x in list(str(i))])
    dicionario[i] = soma

for _ in range(int(input())):
    imprimir(dicionario[int(input())])
