quantidade = 0
for i in range(1000, 10000):
    numero = str(i)
    valido = True
    for j in range(1, len(numero)):
        digito = int(numero[j])
        anterior = int(numero[j - 1])
        if(digito - 1 == anterior or digito + 1 == anterior or digito == anterior):
            valido = False
            break
    if(valido):
        print(numero, end=' ')
        quantidade += 1
print("A quantidade máxima é: " + str(quantidade))