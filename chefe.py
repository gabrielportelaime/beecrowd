while(True):
    try:
        vertices, arestas, consultas = [int(x) for x in input().split()]
        idades = [int(x) for x in input().split()]
        idades.insert(0, 0)
        adjacencias = []
        for i in range(vertices + 1):
            lista = []
            adjacencias.append(lista)
        for i in range(arestas):
            chefe, empregado = [int(x) for x in input().split()]
            adjacencias[chefe].append(empregado)
            
    except EOFError:
        break