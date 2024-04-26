saida = open("C:\\Users\\p001515\\Downloads\\CÓDIGOS\\questoesgitfiltrado.txt", 'r')

entrada = open("C:\\Users\\p001515\\Downloads\\CÓDIGOS\\verifica.txt", 'r')

lista = []
texto = saida.readlines()
for frase in texto:
    lista.append(int(frase))

texto = entrada.readlines()
for frase in texto:
    problema = int(frase.split(' - ')[0])
    if(problema in lista):
        print(problema)