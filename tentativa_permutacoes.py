from itertools import permutations  

palavra = "GOIABADA"
perm = permutations(list(palavra))  

contador = 0
for i in list(set(perm)):
    anagrama = ''.join(i)
    igual = False 
    for j in range(len(palavra)):
        if(anagrama[j] == palavra[j]):
            igual = True
            break
    if(not igual):
        contador += 1
print(contador)
