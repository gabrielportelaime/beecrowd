for i in range(int(input())):
    palavra = input()
    lista = list(palavra)
    lista.sort()
    print(''.join(lista[1::]))