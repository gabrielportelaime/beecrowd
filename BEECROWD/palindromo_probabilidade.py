from itertools import permutations  

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

a = "PALINDROMO"
permutacoes = permutations(a)
lista = list(set(permutacoes))
tamanho = len(lista)
contador = 0
for i in range(len(lista)):
    anagrama = ''.join(lista[i])
    if(anagrama.index('A') < anagrama.index('I') and anagrama.index('A') < anagrama.index('O')):
        if(anagrama.index('I') < anagrama.index('O')):
            contador += 1
maximo = mdc(contador, tamanho)
print(contador, tamanho)
while(maximo != 1):
    contador = contador//maximo
    tamanho = tamanho//maximo
    maximo = mdc(contador, tamanho)
print(str(contador) + '/' + str(tamanho)) 

