def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


print('\n', get_matrix(4, 3, 11),
      '\n', get_matrix(2, 2, 2),
      '\n', get_matrix(3, 5, 3),
      '\n', get_matrix(1, 1, 5)
      )