telefone = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
entrada = input()
saida = ""
for letra in entrada:
    if(letra in letras):
        for i in range(len(telefone)):
            if(letra in telefone[i]):
                saida += str(i + 2)
    else:
        saida += letra
print(saida)