class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

def kruskal(graph):
    num_vertices = len(graph)
    edges = []
    for u in range(num_vertices):
        for v, weight in graph[u]:
            edges.append((weight, u, v))
    edges.sort()
    mst = []
    uf = UnionFind(num_vertices)
    total_cost = 0
    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight
    return total_cost


for i in range(int(input())):
    pontos = []
    vertices = int(input())
    graph = []
    for j in range(vertices):
        lista = []
        graph.append(lista)
    for j in range(vertices):
        x, y = [int(x) for x in input().split()]
        pontos.append([x, y])
    for j in range(len(pontos)-1):
        for k in range(j + 1, len(pontos)):
            distancia = ((pontos[j][0] - pontos[k][0])**2+(pontos[j][1] - pontos[k][1])**2)**(1/2)
            graph[j].append((k, distancia))
            graph[k].append((j, distancia))
    
    custo = kruskal(graph)
    print(f"{custo/100:.2f}")
