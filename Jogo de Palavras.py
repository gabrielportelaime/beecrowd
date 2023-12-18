caso = 1
while True:
    palavra = input()
    if(palavra == "*"):
        break
    palavras = [palavra]
    for i in range(len(palavra) - 1):
        palavra = palavra[-1] + palavra[:-1:]
        palavras.append(palavra)
    palavras.sort()
    print(f"Caso {caso}:", palavras[0], palavras[-1])
    caso += 1