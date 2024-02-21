
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

for _ in range(int(input())):
    tamanho = int(input())
    imprimiu = False
    for i in range(1, 27):
        for j in range(1, 27):
            for k in range(1, 27):
                if(i + j + k == tamanho):
                    imprimir(chr(ord('a') + i - 1) + chr(ord('a') + j - 1) + chr(ord('a') + k - 1))
                    imprimiu = True 
                    break
            if(imprimiu):
                break
        if(imprimiu):
                break