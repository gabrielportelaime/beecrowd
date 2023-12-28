respostas = []
for i in range(int(input())):
    frase = input().split('oulupukk')
    tamanho = len(frase)
    for i in range(tamanho):
        if(i == 0):
            frase[i] = frase[i][:-1:]
        elif(i == tamanho - 1):
            frase[i] = frase[i][1::]
        else:
            frase[i] = frase[i][1:-1:]
    respostas.append("Joulupukki".join(frase))

print('\n'.join(respostas))