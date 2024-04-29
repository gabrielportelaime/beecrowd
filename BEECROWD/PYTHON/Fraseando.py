minha_string = input()
dicionario = {}
contador = 0
for i in range(len(minha_string)):
    if(minha_string[i] not in dicionario):
        dicionario[minha_string[i]] = chr(ord('a') + contador)
        contador += 1
        print(dicionario[minha_string[i]], end='')
    else:
        print(dicionario[minha_string[i]], end='')
print('')