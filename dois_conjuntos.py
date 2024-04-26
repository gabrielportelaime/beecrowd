entrada = [1, 2, 5, 6, 7, -1, 2, 3, 0, 4, 9]
soma = sum(entrada)
if(soma%2 == 1):
    print("impossível")
else:
    entrada.sort()
    for i in range(len(entrada)):
        print('a')
    print("possível")