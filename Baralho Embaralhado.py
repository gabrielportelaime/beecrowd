import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

cartas = int(input())
x = 2
y = 1
while(x != 1):
    media = cartas//2
    if(x <= media):
        x += x
    else:
        x -= cartas - x + 1
    y += 1
imprimir(y)