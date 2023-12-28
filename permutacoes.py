from itertools import combinations
quantidade, minimo, maximo = [int(x) for x in input().split()]
numeros = [int(x) for x in input().split()]
perm = combinations(numeros, 2)
total = 0
for i in list(perm):
    soma = i[0] + i[1]
    if(soma <= maximo and soma >= minimo):
        total += 1
print(total)