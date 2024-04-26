import os, sys, io

input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto, end="\n"):
    sys.stdout.write(str(texto) + end)


for i in range(int(input())):
    n, tirar, colocar = [int(x) for x in input().split()]
    lista = [int(x) for x in input().split()]
    lista.sort()
    lista_sem_repeticao = []
    resposta = 0
    for numero in lista:
        if(len(lista_sem_repeticao) == 0):
            lista_sem_repeticao.append(numero)
        else:
            if(numero != lista_sem_repeticao[-1]):
                lista_sem_repeticao.append(numero)
            else:
                resposta += tirar
    