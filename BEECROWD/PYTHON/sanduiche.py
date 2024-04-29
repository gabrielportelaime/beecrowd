while(True):
    frase = input()
    remover = ''
    while(remover in frase):
        frase = frase[:-1:]
        remover += frase[-1]