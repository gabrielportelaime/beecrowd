import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

def contida (a, b):
    for i in range(len(a)):
        if(a[i] not in b):
            return False
    return True

lista = 'AHIMOTUVWXY'
respostas = []

for _ in range(int(input())):
    palavra = input()
    tamanho = len(palavra)
    achou = False
    for i in range(tamanho, 1, -1):
        for j in range(tamanho - i + 1):
            palavra_normal = palavra[j:j+i]
            palavra_inversa = palavra_normal[::-1]
            if(palavra_normal == palavra_inversa and contida(palavra_normal, lista)):
                respostas.append(str(len(palavra[j:j+i])))
                achou = True
                break
        if(achou):
            break
    if(not achou):
        respostas.append('1')
print('\n'.join(respostas))