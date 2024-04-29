import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

respostas = []

for i in range(int(input())):
    esfera = int(input())
    if(esfera < 1809):
        respostas.append(f"{'vermelho'} = R$ {0.09*esfera:.2f}")
    elif(esfera <= 2826):
        respostas.append(f"{'azul'} = R$ {0.07*esfera:.2f}")
    else:
        respostas.append(f"{'amarelo'} = R$ {0.05*esfera:.2f}")

imprimir('\n'.join(respostas))