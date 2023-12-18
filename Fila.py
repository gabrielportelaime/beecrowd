import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

input()
fila = input().split()
input()
remover = input().split()

for id in remover:
    fila.remove(id)

imprimir(' '.join(fila))