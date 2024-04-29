
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

for _ in range(int(input())):
    respostas = 0
    n, m, k = [int(x) for x in input().split()]
    lista1 = [int(x) for x in input().split()]
    lista2 = [int(x) for x in input().split()]
    for i in range(n):
        for j in range(m):
            if(lista1[i] + lista2[j] <= k):
                respostas += 1
    imprimir(respostas)