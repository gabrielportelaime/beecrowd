quantidade = int(input())
entrada = list(input())
anterior = entrada[0]
quantidade = 0
for caracter in entrada:
    if(caracter == anterior):
        quantidade += 1
    else:
        print(quantidade, anterior, end=" ")
        anterior = caracter
        quantidade = 0
print(quantidade, anterior)