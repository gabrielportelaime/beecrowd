import math
import time
inicio = time.time()
n = 100
soma = 0
for i in range(math.floor(math.log10(n))):
    soma += (10**i)*(math.floor((n - 9*(10**i))/(10**(i+1))) + 1)
print(soma)
fim = time.time()
matematica = fim - inicio
print(matematica)
inicio = time.time()
numeros = []
for i in range(n):
    numeros.append(str(i))
print("".join(numeros).count('9'))
fim = time.time()
conta_caracteres = fim - inicio
print(conta_caracteres)
print("Matemática é:", math.ceil(conta_caracteres/matematica), "vezes mais rapido")