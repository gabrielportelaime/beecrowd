respostas = []

for i in range(int(input())):
    numero = list(input().replace('\r', ''))
    numero.sort()
    zeros = ""
    sorte = ""
    ja = True
    for j in range(len(numero)):
        if(numero[j] == '0'):
            zeros += '0'
        else:
            sorte += numero[j]
            if(ja):
                sorte += zeros
                ja = False
    respostas.append(sorte)

print('\n'.join(respostas))