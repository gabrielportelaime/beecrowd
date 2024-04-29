
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

for _ in range(int(input())):
    palavra = input()
    if(palavra.count('A') > palavra.count('B')):
        imprimir('A')
    else:
        imprimir('B')