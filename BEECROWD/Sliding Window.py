lista = [0, 1, 1, 1, 0, 1, 1, 1]
antes = depois = maior = zeros = 0
for i in range(len(lista)):
    if(lista[i] == 1 and zeros == 0):
        antes += 1
    elif(lista[i] == 1 and zeros == 1):
        depois += 1
    elif(lista[i] == 0 and zeros == 0):
        zeros += 1
    elif(lista[i] == 0 and zeros == 1):
        if(antes + depois > maior):
            maior = antes + depois
        antes = depois
        depois = 0
        zeros = 1
if(antes + depois > maior):
    maior = antes + depois
print(maior)
