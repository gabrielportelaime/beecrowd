import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

respostas = []

alfabeto = ""
for i in range(1, 27):
    alfabeto += chr(i + 64)

quantidade = int(input())
while(quantidade != 0):
    lista = [int(x) for x in input().split()]
    resposta = []
    for i in range(quantidade):
        letra = alfabeto[lista[i] - 1]
        resposta.append(letra)
        metade_inicial = alfabeto[:lista[i]-1]
        metade_final = alfabeto[lista[i]::]
        alfabeto = letra+metade_inicial+metade_final
    quantidade = int(input())
    respostas.append(resposta)

for i in range(len(respostas)):
    imprimir(''.join(respostas[i]))