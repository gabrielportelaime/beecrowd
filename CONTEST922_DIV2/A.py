
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

for _ in range(int(input())):
    a, b = map(int, input().split())
    imprimir(a*int(b/2))