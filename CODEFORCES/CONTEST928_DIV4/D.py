
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]
from collections import deque

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

respostas = []
for _ in range(int(input())):
    tamanho = int(input())
    dicionario = {}
    entrada = [int(x) for x in input().split()]
    conjunto = set(entrada)
    lista = deque(entrada)
    total = tamanho
    while(len(lista) > 0):
        barrado = 2147483648 + ~(lista[0])
        dicionario[barrado] = lista[0]
        try:
            tem = dicionario[lista[0]]
            total -= 1
        except:
            print('', end='')
        lista.popleft()
    respostas.append(str(total + (len(lista) - len(conjunto))//2))
imprimir("\n".join(respostas))