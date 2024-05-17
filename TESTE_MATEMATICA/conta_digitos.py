numeros = []
n = 120387
algarismo = 5

for i in range(n + 1):
    numeros.append(str(i))
print("".join(numeros).count(str(algarismo)))

digitos = str(n)
tamanho = len(digitos)
qtd_digitos = 0
sufixo = []
soma_parcial = 0
algarismo = 5
for i in range(tamanho - 1, -1, -1):
    digito = digitos[i]
    potencia = tamanho - i
    if(int(digito) == algarismo):
        if(len(sufixo) > 0):
            soma_parcial = (n//(10**potencia))*10**(potencia - 1) + int("".join(sufixo)[::-1]) + 1
        else:
            soma_parcial = (n//(10**potencia))*10**(potencia - 1) + 1
    elif(int(digito) > algarismo):
        soma_parcial =  (n//(10**potencia) + 1)*10**(potencia - 1)
    else:
        soma_parcial =  (n//(10**potencia))*10**(potencia - 1)
    qtd_digitos += soma_parcial
    sufixo.append(digito)
print(qtd_digitos)