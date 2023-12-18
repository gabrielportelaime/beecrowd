import os, sys, io

input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto, end="\n"):
    sys.stdout.write(str(texto) + end)

qtd_proc, cores, tempo_total = [int(x) for x in input().split()]

processos = []

for i in range(qtd_proc):
    processos.append([int(x) for x in input().split()])

processos.sort(key=lambda c: (c[0], c[3]))

imprimir(processos)