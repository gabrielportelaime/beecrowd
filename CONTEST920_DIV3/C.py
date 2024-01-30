import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

respostas = []
for _ in range(int(input())):
    tempo = 0
    deu = True
    n, f, a, b = [int(x) for x in input().split()]
    mensagens = [int(x) for x in input().split()]
    for i in range(n):
        if((mensagens[i] - tempo)*a < b):
            if((mensagens[i] - tempo)*a < f):
                f -= (mensagens[i] - tempo)*a
                tempo = mensagens[i]
            else:
                respostas.append('NO')
                deu = False
                break
        elif(b < f):
            f -= b
            tempo = mensagens[i]
        else:
            respostas.append('NO')
            deu = False
            break
    if(deu):
        respostas.append('YES')

imprimir('\n'.join(respostas))