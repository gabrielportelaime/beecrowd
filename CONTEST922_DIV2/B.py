
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

for _ in range(int(input())):
    tamanho = int(input())
    lista1 = [int(x) for x in input().split()]
    lista2 = [int(x) for x in input().split()]
    lista = []
    for i in range(tamanho):
        lista.append((lista1[i], lista2[i]))
    lista.sort()
    lista1 = []
    lista2 = []
    for i in range(tamanho):
        lista1.append(lista[i][0])
        lista2.append(lista[i][1])
    print(' '.join([str(x) for x in lista1]))
    print(' '.join([str(x) for x in lista2]))