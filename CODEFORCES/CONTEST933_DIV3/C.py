
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

respostas = []
for _ in range(int(input())):
    tamanho = int(input())
    palavra = input()
    resposta = palavra.count('mapie')
    palavra = palavra.replace('mapie', 'maie')
    resposta += palavra.count('pie') + palavra.count('map')
    palavra = palavra.replace('map', 'mp')
    palavra = palavra.replace('pie', 'pe')
    respostas.append(str(resposta))
imprimir('\n'.join(respostas))