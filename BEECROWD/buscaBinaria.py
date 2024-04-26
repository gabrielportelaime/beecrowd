import time 

def busca_binaria(lista, item):
    primeiro = 0
    ultimo = len(lista) - 1
    achou = False
    while primeiro <= ultimo and not achou:
        meio = (primeiro + ultimo) // 2
        if lista[meio] == item:
            achou = True
        else:
            if item < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return achou

#gerar os grupos
qtd_grupos = 100000
usuario_por_grupo = 1024
grupos = []
usuarios = []
for i in range(qtd_grupos):
    grupo = []
    for j in range(usuario_por_grupo):
        usuario = i*usuario_por_grupo + j
        grupo.append(usuario)
        usuarios.append(usuario)
    grupos.append(grupo)

#grupos gerados e estrutura pronta
usuario_buscado = 100000000
#Teste 1: busca simples
inicio = time.time()
achou = False
for i in range(len(grupos)):
    if(usuario_buscado in grupos[i]):
        achou = True
        break
print('Busca simples:')
print('Usuario está nos grupos?')
print(achou)
fim = time.time()
print(fim - inicio)
#Teste 2: busca binaria
usuarios.sort()
inicio = time.time()
print('Busca Binária:')
print('Usuario está nos grupos?')
print(busca_binaria(usuarios, usuario_buscado))
fim = time.time()
print(fim - inicio)