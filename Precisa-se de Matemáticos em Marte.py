import os, sys, io

input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto, end="\n"):
    sys.stdout.write(str(texto) + end)

somas = {}
quantidade = int(input())
buggies = [int(x) for x in input().split()]
soma = 0
for i in range(quantidade):
    somas[i + 1] = soma
    soma += buggies[i]

respostas = []

while True:
    try:
        opcao, valor = input().split()
        valor = int(valor)
        if(opcao == 'a'):
            for i in range(valor, quantidade + 1):
                somas[i] -= buggies[valor - 1]
        else:
            imprimir(somas[valor])
    except EOFError:
        break