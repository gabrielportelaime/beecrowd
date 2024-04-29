import os, sys, io
from collections import deque
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

respostas = []
for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    vania = [int(x) for x in input().split()]
    maluco = [int(x) for x in input().split()]
    vania.sort()
    maluco.sort(reverse=True)
    vania = deque(vania)
    maluco = deque(maluco)
    diferenca = 0
    while(len(vania) > 0):
        if(abs(maluco[0] - vania[0]) > abs(maluco[-1] - vania[-1])):
            diferenca += abs(maluco[0] - vania[0])
            maluco.popleft()
            vania.popleft()
        else:
            diferenca += abs(maluco[-1] - vania[-1])
            maluco.pop()
            vania.pop()
    respostas.append(str(diferenca))

imprimir('\n'.join(respostas))