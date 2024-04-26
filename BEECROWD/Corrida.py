import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

numero, distancia, velocidade = map(int, input().split())
numero1, distancia2, velocidade2 = map(int, input().split())

if(distancia/velocidade < distancia2/velocidade2):
    imprimir(numero)
else:
    imprimir(numero1)