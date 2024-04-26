import itertools

def valor(tupla):
    minimo = 2**30
    for i in range(len(tupla) - 1):
        for j in range(i + 1, len(tupla)):
            minimo = min(tupla[i]^tupla[j], minimo)
    return minimo

def findsubsets(s, n):
    return list(itertools.combinations(s, n))

quantidade = int(input())

lista = [int(x) for x in input().split()]

subconjuntos = []

for i in range(1, len(lista)):
    for j in findsubsets(lista, i):
        subconjuntos.append(j)

maximo = -1

for i in range(len(subconjuntos)//2):
    valor_conjunto = min(valor(subconjuntos[i]), valor(subconjuntos[-i-1]))
    if(valor_conjunto >= maximo):
        subconjunto = subconjuntos[i]
        maximo = valor_conjunto

for elemento in lista:
    if(elemento in subconjunto):
        print('1', end="")
    else:
        print('0', end="")
print("")