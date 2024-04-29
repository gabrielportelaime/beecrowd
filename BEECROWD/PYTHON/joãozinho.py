import itertools 
import math

def mmc (a, b):
    return (a*b)//mdc(a, b)

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

while(True):
    inicio, fim, n = [int(x) for x in input().split()]
    if(inicio == fim == n == 0):
        break
    caminhoes = set()
    for i in range(n):
        caminhoes.add(int(input()))
    soma = 0
    for i in range(1, len(caminhoes) + 1, 2):
        subconjuntos = list(itertools.combinations(caminhoes, i))
        for tupla in subconjuntos:
            min_mul_com = 1
            for valor in tupla:
                min_mul_com = mmc(min_mul_com, valor)
                comeco = math.ceil(inicio/min_mul_com)
                final = math.floor(fim/min_mul_com)
                soma += ((final - comeco + 2)*(final - comeco + 1))//2
    for i in range(2, len(caminhoes) + 1, 2):
        subconjuntos = list(itertools.combinations(caminhoes, i))
        for tupla in subconjuntos:
            min_mul_com = 1
            for valor in tupla:
                min_mul_com = mmc(min_mul_com, valor)
                comeco = math.ceil(inicio/min_mul_com)
                final = math.floor(fim/min_mul_com)
                soma -= ((final - comeco + 2)*(final - comeco + 1))//2
    print(soma%1300031)

