import os, sys, io

input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto, end="\n"):
    sys.stdout.write(str(texto) + end)

n, m = [int(x) for x in input().split()]
guildas = []

while(n != 0 and m != 0):
    pontos = [int(x) for x in input().split()]
    for i in range(m):
        q, a, b = [int(x) for x in input().split()]
    n, m = [int(x) for x in input().split()]
    guildas = []