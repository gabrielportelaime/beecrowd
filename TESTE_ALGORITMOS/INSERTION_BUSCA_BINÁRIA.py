import random
import time

def adicionar_com_busca_binaria(lista , elemento):
    tamanho = len(lista)
    if(tamanho == 0):
        lista.append(elemento)
        return lista
    comeco = 0
    fim = tamanho - 1
    indice_elemento_do_meio = (comeco + fim) // 2
    elemento_do_meio = lista[indice_elemento_do_meio]
    encontrado = True
    while encontrado:
        if(comeco == fim):
            if(elemento_do_meio > elemento):
                lista.insert(indice_elemento_do_meio - 1, elemento)
                return lista
            else:
                lista.insert(indice_elemento_do_meio + 1, elemento)
                return lista
        elif(elemento_do_meio == elemento):
            lista.insert(indice_elemento_do_meio, elemento)
            return lista
        elif(elemento_do_meio > elemento):
            nova_posicao = indice_elemento_do_meio - 1
            fim = nova_posicao
            indice_elemento_do_meio = (comeco + fim) // 2
            elemento_do_meio = lista[indice_elemento_do_meio]
            if(elemento_do_meio == elemento):
                lista.insert(indice_elemento_do_meio, elemento)
                return lista
        elif(elemento_do_meio < elemento):
            nova_posicao = indice_elemento_do_meio + 1
            comeco = nova_posicao
            fim = tamanho - 1
            indice_elemento_do_meio = (comeco + fim) // 2
            elemento_do_meio = lista[indice_elemento_do_meio]
            if(elemento_do_meio == elemento):
                lista.insert(indice_elemento_do_meio, elemento)
                return lista

def ordenar_busca_binaria(lista):
    lista_ordenada = []
    for elemento in lista:
        lista_ordenada = adicionar_com_busca_binaria(lista_ordenada, elemento)
        print(lista_ordenada)

lista = [100, 200, 8, 1, 10, 50 , 60 , 81 , 84 , 89]
ordenar_busca_binaria(lista)

# quantidade_numeros = 10000000
# range_numeros = quantidade_numeros*100
# lista = []

# for i in range(quantidade_numeros):
#     x = random.randint(1, range_numeros)
#     lista.append(x)

# tempo_inicio = time.time()
# lista_ordenada = sorted(lista)
# tempo_fim = time.time()

# print(tempo_fim - tempo_inicio)