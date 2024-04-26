import os, sys, io

input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto, end="\n"):
    sys.stdout.write(str(texto) + end)

v, m = [int(x) for x in input().split()]
moedas = [int(x) for x in input().split()]

