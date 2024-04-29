
import os, sys, io
from collections import deque
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

respostas = []
for _ in range(int(input())):
    jogadores_atual = []
    jogadores_bola = []
    jogadores, lancamentos, jogador = [int(x) for x in input().split()]
    jogadores_atual.append(jogador)
    for i in range(lancamentos):
        entrada = input()
        lancado = int(entrada[:-1:])
        if(entrada[-1] == '?'):
            for j in range(len(jogadores_atual)):
                anti = (jogadores_atual[j] - lancado)%jogadores
                horario = (jogadores_atual[j] + lancado)%jogadores
                if(anti == 0):
                    anti = jogadores
                if(horario == 0):
                    horario = jogadores
                jogadores_bola.append(anti)
                jogadores_bola.append(horario)
        elif(entrada[-1] == '1'):
            for j in range(len(jogadores_atual)):
                anti = (jogadores_atual[j] - lancado)%jogadores
                if(anti == 0):
                    anti = jogadores
                jogadores_bola.append(anti)
        elif(entrada[-1] == '0'):
            for j in range(len(jogadores_atual)):
                horario = (jogadores_atual[j] + lancado)%jogadores
                if(horario == 0):
                    horario = jogadores
                jogadores_bola.append(horario)
        jogadores_bola = list(set(jogadores_bola))
        jogadores_atual = jogadores_bola
        jogadores_bola = []
    jogadores_atual.sort()
    imprimir(len(jogadores_atual))
    imprimir(' '.join([str(x) for x in jogadores_atual]))