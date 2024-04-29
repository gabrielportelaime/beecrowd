
import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

for _ in range(int(input())):
    tamanho = int(input())
    formato = "SQUARE"
    for i in range(tamanho):
        linha = input()
        for j in range(1, tamanho - 1):
            if(linha[j] == '1' and linha[j - 1] == '0' and linha[j + 1] == '0'):
                formato = "TRIANGLE"
                break
    imprimir(formato)