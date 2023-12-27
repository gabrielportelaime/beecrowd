import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

entrada = input()
respostas = []
while(entrada != "0+0=0"):
    n1 = entrada.split("+")[0]
    n2 = entrada.split("+")[1].split("=")[0]
    res = entrada.split("+")[1].split("=")[1]
    n1 = n1[::-1]
    n2 = n2[::-1]
    res = res[::-1]
    respostas.append(str(int(n1) + int(n2) == int(res)))
    entrada = input()

respostas.append('True')
imprimir('\n'.join(respostas))