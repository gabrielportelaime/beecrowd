chave = input()

matriz = []

for i in range(26):
    lista = []
    for j in range(26):
        lista.append(chr((i+j)%26 + ord('a')))
    matriz.append(lista)

for i in range(int(input())):
    frases = input().split(" ")
    criptos = []
    contador = 0
    for frase in frases:
        if(frase[0] not in "aeiou"):
            tamanho = len(frase)
            cripto = ''
            for j in range(tamanho):
                if(frase[j] != ' '):
                    linha = ord(chave[contador]) - ord('a')
                    coluna = ord(frase[j]) - ord('a')
                    cripto += matriz[linha][coluna]
                    contador += 1
                    if(contador == len(chave)):
                        contador = 0
                else:
                    cripto += ' '
            criptos.append(cripto)
        else:
            criptos.append(frase)
    print(" ".join(criptos))   


