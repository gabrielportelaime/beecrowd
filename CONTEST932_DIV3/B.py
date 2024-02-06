
from collections import deque
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

for _ in range(int(input())):
    tamanho = int(input())
    traco = [int(x) for x in input().split()]
    alfa = [deque([chr(ord('a') + i) for i in range(26)])]
    for i in range(tamanho + 1):
        alfa.append(deque(list()))
    palavra = []
    for i in range(tamanho):
        letra = alfa[traco[i]][0]
        palavra.append(letra)
        alfa[traco[i]].popleft()
        alfa[traco[i] + 1].append(letra)
    imprimir(''.join(palavra))