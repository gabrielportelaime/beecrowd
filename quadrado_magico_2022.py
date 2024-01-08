matriz = []
n = int(input())
for i in range(n):
    linha = [int(x) for x in input().split()]
    matriz += linha
    for j in range(n):
        if(linha[j] == 0):
            nr_linha = i + 1
            nr_coluna = j + 1
            break
matriz.sort()
imprimiu = False
for i in range(n*n):
    if(i != matriz[i]):
        print(i)
        imprimiu = True
        break
if(not imprimiu):
	print(n*n)
print(nr_linha)
print(nr_coluna)