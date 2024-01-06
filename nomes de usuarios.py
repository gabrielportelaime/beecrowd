import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

while True:
    entrada = input().split()
    if not entrada:
        break
    alunos = int(entrada[0])
    ano = entrada[1]
    users = set()
    quantidade = 0
    for i in range(alunos):
        nomes = input().split()
        user = ""
        for nome in nomes:
            user += nome[0]
        users.add(user)
    imprimir(alunos - len(users))