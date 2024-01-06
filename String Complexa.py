tam_string = int(input())
minha_string = input()
apareceram = []
contador = 0
for i in range(tam_string):
    if(minha_string[i] not in apareceram):
        apareceram.append(minha_string[i])
        contador += 1
if(contador >= 3):
    print('Yes')
else:
    print('No')