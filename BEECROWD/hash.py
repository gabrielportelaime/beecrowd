saidas = []
for i in range(int(input())):
    saidas.append(input().strip())
conjunto = set(saidas)
if(len(conjunto) == len(saidas)):
    print('A funcao eh boa.')
else:
    print('A funcao nao eh boa.')