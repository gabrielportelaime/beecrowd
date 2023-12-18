import os, sys, io

input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto, end="\n"):
    sys.stdout.write(str(texto) + end)

while True:
    try:
        fita = list(input())
        contador = 0
        continua = True
        while(continua):
            continua = False
            for i in range(len(fita) - 1):
                caso1 = fita[i] == 'S' and fita[i + 1] == 'B'
                caso2 = fita[i] == 'B' and fita[i + 1] == 'S'
                caso3 = fita[i] == 'C' and fita[i + 1] == 'F'
                caso4 = fita[i] == 'F' and fita[i + 1] == 'C'
                if(caso1 or caso2 or caso3 or caso4):
                    fita.pop(i)
                    fita.pop(i)
                    contador += 1
                    continua = True
                    break
        imprimir(contador)
    except EOFError:
        break
