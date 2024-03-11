
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

for _ in range(int(input())):
    respostas = 0
    vertices, arestas = [int(x) for x in input().split()]
    grafo = []
    linhas = {}
    for i in range(arestas):
        origem, destino, linha = [int(x) for x in input().split()]
    origem, destino = [int(x) for x in input().split()]
    imprimir(respostas)