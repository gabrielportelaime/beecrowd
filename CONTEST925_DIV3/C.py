import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

respostas = []
for _ in range(int(input())):
    tamanho = int(input())
    lista = [int(x) for x in input().split()]
    if(lista.count(lista[0]) == tamanho):
        respostas.append('0')
    else:
        inicio = fim = maior = 1
        for i in range(1, tamanho):
            if(lista[i] == lista[0]):
                inicio += 1
            else:
                break
        for i in range(2, tamanho):
            if(lista[-i] == lista[-1]):
                fim += 1
            else:
                break
        if(lista[0] == lista[-1]):
            respostas.append(str(tamanho - inicio - fim))
        elif(inicio > fim):
            respostas.append(str(tamanho - inicio))
        else:
            respostas.append(str(tamanho - fim))
imprimir('\n'.join(respostas))