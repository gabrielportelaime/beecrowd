import math
for n in range(1, 1000):
    soma = 0
    for i in range(math.floor(math.log10(n)) + 1):
        soma += (10**i)*(math.floor((n - 10**i)/(10**(i+1))) + 1)
    numeros = []
    for i in range(n + 1):
        numeros.append(str(i))
    if(soma == "".join(numeros).count('1')):
        print(n, soma, "-","".join(numeros).count('1'), "OK")
    else:
        print(n, soma, "-","".join(numeros).count('1'), "ERROR")