numeros = []
n = 7456
for i in range(n + 1):
    numeros.append(str(i))
print("".join(numeros).count('1'))