vertices, qtd_arestas = [int(x) for x in input().split()]
input()
arestas = []
for i in range(qtd_arestas):
    v1, v2, peso = [int(x) for x in input().split()]
    arestas.append([peso, v1-1, v2-1])
total = 0
arvore = []
A = []
for i in range(vertices):
    setV = {i}
    arvore.append(setV)
arestas.sort()
for aresta in arestas:
    peso, v1, v2 = aresta
    if(arvore[v1] != arvore[v2]):
        arvore[v1] = arvore[v1] | arvore[v2]
        arvore[v2] = arvore[v1] | arvore[v2]
        A.append(aresta[0])

print(sum(A)*2)
