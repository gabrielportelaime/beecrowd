import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

for _ in range(int(input())):
    tamanho = int(input())
    atual = [int(x) for x in list(input())]
    futuro = [int(x) for x in list(input())]
    soma_atual = sum(atual)
    soma_futuro = sum(futuro)
    resposta = min(soma_atual, soma_futuro) + abs(soma_futuro-soma_atual)
    imprimir(resposta)