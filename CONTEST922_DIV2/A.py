
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

for _ in range(int(input())):
    a, b = map(int, input().split())
    imprimiu = False
    for i in range(3):
        c, d = map(int, input().split())
        if(a == c and not imprimiu):
            print((abs(d-b))**2)
            imprimiu = True
        elif(b == d and not imprimiu):
            print((abs(a-c))**2)
            imprimiu = True
        else:
            continue