
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

for _ in range(int(input())):
    tamanho = int(input())
    faixa = input()
    lista_faixa = list(faixa)
    if(lista_faixa.count('B')  == 0):
        imprimir('0')
    elif(lista_faixa.count('B') == 1):
        imprimir('1')
    else:
        for i in range(1, tamanho):
            if(lista_faixa[-i] == 'B'):
                break
        imprimir(tamanho - i - faixa.index('B') + 1)