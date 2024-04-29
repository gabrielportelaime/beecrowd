import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

dinheiro, transacoes = map(int, input().split())

jogadores = {'D': dinheiro, 'E': dinheiro, 'F': dinheiro}

respostas = []

for i in range(transacoes):
    acao = input().split()
    if(acao[0] == 'C'):
        jogadores[acao[1]] -= int(acao[2])
    elif(acao[0] == 'V'):
        jogadores[acao[1]] += int(acao[2])
    else:
        jogadores[acao[1]] += int(acao[3])
        jogadores[acao[2]] -= int(acao[3])

for chave, valor in jogadores.items():
    respostas.append(str(valor))

imprimir(' '.join(respostas))