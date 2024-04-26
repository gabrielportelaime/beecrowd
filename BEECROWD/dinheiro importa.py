vertices, arestas = [int(x) for x in input().split()]

pessoas = []
grafo = []

for i in range(vertices):
    lista = {i}
    pessoas.append(int(input()))
    grafo.append(lista)


for i in range(arestas):
    v1, v2 = [int(x) for x in input().split()]
    for conjunto in grafo:
        if(v1 in conjunto):
            conj1 = conjunto
        if(v2 in conjunto):
            conj2 = conjunto
    if(conj1 != conj2):
        grafo.remove(conj1)
        grafo.remove(conj2)
        conj1 = conj1 | conj2
        grafo.append(conj1)
possivel = True
for conjunto in grafo:
    soma = 0
    for vertice in conjunto:
        soma += pessoas[vertice]
    if(soma != 0):
        possivel = False
        break
if(possivel):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
