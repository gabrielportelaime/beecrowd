import os, sys, io

input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto, end="\n"):
    sys.stdout.write(str(texto) + end)

# while True:
#     try:

#     except EOFError:
#         break

numeros = []
n = 10000

for i in range(n + 1):
    numeros.append(str(i))
print(sum([int(x) for x in "".join(numeros)]))

