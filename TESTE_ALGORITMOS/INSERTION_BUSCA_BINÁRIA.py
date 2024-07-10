import random
import time

def busca_binaria(lista , elemento):
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
        if comeco == fim:
            if elemento_do_meio != elemento:
                encontrado = False
                return "Não aparece na lista"

        elif elemento_do_meio == elemento:
            return f"{elemento_do_meio} encontrado na posição {indice_elemento_do_meio}"

        elif elemento_do_meio > elemento:
            nova_posicao = indice_elemento_do_meio - 1
            fim = nova_posicao
            indice_elemento_do_meio = (comeco + fim) // 2
            elemento_do_meio = lista[indice_elemento_do_meio]
            if elemento_do_meio == elemento:
                return f"{elemento_do_meio} encontrado na posição {indice_elemento_do_meio}"

        elif elemento_do_meio < elemento:
            nova_posicao = indice_elemento_do_meio + 1
            comeco = nova_posicao
            fim = tamanho - 1
            indice_elemento_do_meio = (comeco + fim) // 2
            elemento_do_meio = lista[indice_elemento_do_meio]
            if elemento_do_meio == elemento:
                return f"{elemento_do_meio} encontrado na posição {indice_elemento_do_meio}"



lista = [16 , 18 , 20 , 50 , 60 , 81 , 84 , 89]
print(busca_binaria(lista , 81))
print(busca_binaria(lista , 10))    

# def ordenar_busca_binaria(lista):
    

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