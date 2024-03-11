
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

respostas = []
for _ in range(int(input())):
    tamanho = int(input())
    lista = [int(x) for x in input().split()]
    for i in range(1, tamanho - 1):
        while(lista[i-1] > 0 and lista[i] > 1 and lista[i+1] > 0):
            lista[i-1] -= 1
            lista[i] -= 2
            lista[i+1] -= 1
    if(sum(lista) == 0):
        respostas.append('YES')
    else:
        respostas.append('NO')
imprimir('\n'.join(respostas))