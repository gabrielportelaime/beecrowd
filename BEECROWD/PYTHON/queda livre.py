import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def print_mst(self, parent):
        soma = 0
        for i in range(1, self.V):
            soma += self.graph[i][parent[i]]
        print(f"{soma/100:.2f}")

    def min_key(self, key, mst_set):
        min_value = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min_value and not mst_set[v]:
                min_value = key[v]
                min_index = v

        return min_index

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        mst_set = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for _ in range(self.V - 1):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] >= 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

for i in range(int(input())):
    vertices = int(input())
    g = Graph(vertices)
    pontos = []
    for j in range(vertices):
        x, y = [int(x) for x in input().split()]
        pontos.append([x, y])
    for j in range(len(pontos)-1):
        for k in range(j + 1, len(pontos)):
            distancia = ((pontos[j][0] - pontos[k][0])**2+(pontos[j][1] - pontos[k][1])**2)**(1/2)
            g.add_edge(j, k, distancia)
            g.add_edge(k, j, distancia)
    g.prim_mst()
