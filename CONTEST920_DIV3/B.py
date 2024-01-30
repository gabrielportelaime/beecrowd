import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

respostas = []
for _ in range(int(input())):
    tamanho = int(input())
    atual = [int(x) for x in list(input())]
    futuro = [int(x) for x in list(input())]
    diferenca = abs(sum(futuro) - sum(atual))
    diferentes = 0
    for i in range(tamanho):
        if(atual[i] != futuro[i]):
            diferentes += 1
    resposta = diferenca + (diferentes - diferenca)//2
    respostas.append(str(resposta))

print('\n'.join(respostas))