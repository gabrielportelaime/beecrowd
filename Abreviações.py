import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

frase = input()
while(frase != "."):
    frase = frase.split()
    abreviacoes = []
    quantidade = 0
    for j in range(0, 26):
        letra = chr(ord('a') + j)
        maior = 0
        palavra = ""
        for i in range(len(frase)):
            if(frase[i][0] == letra and len(frase[i]) > 2 and len(frase[i]) > maior):
                maior = len(frase[i])
                palavra = frase[i]
                indice = i
        if(palavra != ""):
            quantidade += 1
            abreviacoes.append(letra + '.' + ' = ' + palavra)
            frase[indice] = letra + '.'
    imprimir(' '.join(frase))
    imprimir(quantidade)
    imprimir('\n'.join(abreviacoes))  
    frase = input()