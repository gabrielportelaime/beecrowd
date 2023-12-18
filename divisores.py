import os, sys, io

input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto, end="\n"):
    sys.stdout.write(str(texto) + end)

def divi (numero):
    divisores = []
    for i in range(2, int((numero)**(1/2)) + 1):
        if(numero%i == 0):
            divisores.append(i)
            divisores.append(numero//i)
    return divisores

a, b, c, d = [int(x) for x in input().split()]
imprimiu = False
divisores = sorted(divi(c))

for i in range(len(divisores)):
    n = divisores[i]
    if(n%a == 0 and n%b != 0 and c%n == 0 and d%n != 0):
        imprimiu = True
        imprimir(n)
        break
    
if(not imprimiu):
    imprimir('-1')