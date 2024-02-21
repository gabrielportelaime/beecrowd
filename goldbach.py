def primo (numero):
    if(numero == 2):
        return True
    if(numero == 1 or numero == 0 or numero%2 == 0):
        return False
    for i in range(3, int((numero)**(1/2)) + 1, 2):
        if(numero%i == 0):
            return False
    return True

limite = 1000001
primos = []
for i in range(2, limite):
    if(primo(i)):
        primos.append(i)

for i in range(4, limite - 2, 2):
    imprimiu = False
    j = 0
    while(primos[j] < i):
        if(primo(i - primos[j])):
            # print(i, '-', primos[j], '+', i - primos[j])
            imprimiu = True
            break
        j += 1
    if(not imprimiu):
        print(i, '- NÃO')
print('ACABOU')