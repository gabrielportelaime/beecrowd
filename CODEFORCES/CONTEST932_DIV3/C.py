from collections import deque
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

def escolher(lista, ka, kb, k, escolhas):
    if(len(escolhas) == k):
        return True
    if(len(escolhas) == 0):
        numero = 1
    else:
        numero = escolhas[-1] + 1
    if(ka > 0 and lista[0][0] == numero and lista[0][1] == 'a'):
        lista.popleft()
        resultado = escolher(lista, ka, kb, k, escolhas)
        escolhas.append(numero)
        return escolher(lista, ka - 1, kb, k, escolhas) or resultado
    if(kb > 0 and lista[0][0] == numero and lista[0][1] == 'b'):
        lista.popleft()
        resultado = escolher(lista, ka, kb, k, escolhas)
        escolhas.append(numero)
        return escolher(lista, ka, kb - 1, k, escolhas) or resultado
    return False
    
for _ in range(int(input())):
    n, m, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    ka = kb = k//2
    lista = []
    for i in range(n):
        lista.append((a[i], 'a'))
    for i in range(m):
        lista.append((b[i], 'b'))
    lista.sort()
    escolhas = []
    imprimir("YES" if escolher(deque(lista), ka, kb, k, escolhas) else "NO")