dados = int(input())
while(dados != 0):
    for i in range(dados):
        numero = input()
        j = 0
        soma1 = soma2 = 0
        for algarismo in numero:
            if(j%2 == 0):
                soma1 += int(algarismo)
            else:
                soma2 += int(algarismo)
            j += 1
        if(soma1 > 9):
            soma1 = sum([int(x) for x in list(str(soma1))])
        if(soma2 > 9):
            soma2 = sum([int(x) for x in list(str(soma2))])
        print(soma1+soma2)
    dados = int(input())