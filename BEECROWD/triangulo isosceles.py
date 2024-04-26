def count_isosceles_triangles(points):
    count = 0
    point_dict = {}

    # Criar um dicionário de pontos, onde a chave é a coordenada (x, y) e o valor é o número de ocorrências
    for point in points:
        if point in point_dict:
            point_dict[point] += 1
        else:
            point_dict[point] = 1

    # Iterar sobre cada ponto
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            # Calcular o ponto médio entre os dois pontos
            mid_point = ((points[i][0] + points[j][0]) / 2, (points[i][1] + points[j][1]) / 2)

            # Calcular o vetor direção do segmento
            direction_vector = (points[j][0] - points[i][0], points[j][1] - points[i][1])

            # Calcular o ponto simétrico em relação ao ponto médio
            symmetrical_point = (mid_point[0] + direction_vector[1], mid_point[1] - direction_vector[0])

            # Verificar se o ponto simétrico existe no conjunto
            if symmetrical_point in point_dict:
                count += point_dict[symmetrical_point]

    return count


# Exemplo de uso
points = [(1, 2), (2, 1), (2, 2), (1, 1), (1000, 1000000)]
count = count_isosceles_triangles(points)
print("Número de triângulos isósceles:", count)
