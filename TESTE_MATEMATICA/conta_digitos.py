import math
n = 13
soma = 0
for i in range(math.floor(math.log10(n))):
    soma += (10**i)*(math.floor((n - 9*(10**i))/(10**(i+1))) + 1)
print(soma)
numeros = []
for i in range(n + 1):
    numeros.append(str(i))
print("".join(numeros).count('9'))
