import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

for _ in range(int(input())):
    tamanho = int(input())
    lista = [int(x) for x in input().split()]
    if(tamanho == 1):
        imprimir('YES')
    else:
        valor = sum(lista)//tamanho
        acumulado = 0
        deu_errado = False
        for i in range(tamanho):
            if(lista[i] >= valor):
                acumulado += lista[i] - valor
            elif(acumulado >= valor - lista[i]):
                acumulado -= valor - lista[i]
            else:
                imprimir('NO')
                deu_errado = True
                break
        if(not deu_errado):
            imprimir('YES')