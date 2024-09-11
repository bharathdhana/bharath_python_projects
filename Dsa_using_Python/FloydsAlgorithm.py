def floyd(graph):
    distance_matrix = [[float('inf') if i != j else 0 for j in range(len(graph))] for i in range(len(graph))]

    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != 0:
                distance_matrix[i][j] = graph[i][j]

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if distance_matrix[i][k] + distance_matrix[k][j] < distance_matrix[i][j]:
                    distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]

    print("The shortest distance matrix is:")
    for row in distance_matrix:
        print(row)

I = float('inf')
adjMatrix = [
    [0, 1, -2, 1],
    [4, 0, 3, 1],
    [1, 1, 0, 2],
    [1, -1, 1, 0]
]

floyd(adjMatrix)
