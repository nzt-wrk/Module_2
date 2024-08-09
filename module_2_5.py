def get_matrix(n, m, value):
    matrix = []
    #set1 = []
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


# print()

# n = int(input("Кол-во строк: "))
# m = int(input("Кол-во столбцов: "))
# value = int(input("Значения матрицы: "))
# result = get_matrix(n, m, value)
#
# print(result)

