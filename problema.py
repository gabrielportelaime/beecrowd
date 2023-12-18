nomes = []
for i in range(int(input())):
    nome = input()
    nomes.append(nome)

for i in range(26):
    for nome in nomes:
        if(nome[0] == chr(ord('A')+i)):
            print(nome)
