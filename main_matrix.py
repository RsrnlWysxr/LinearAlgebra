from playLA.Matrix import Matrix

if __name__ == '__main__':
    matrix = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])

    print("{}".format(matrix))

    print(matrix.shape())

    print("matrix[0][1] = {}".format(matrix[0, 1]))

    print("matrix_row[1] = {}".format(matrix.row_vector(1)))

    print("matrix_col[1] = {}".format(matrix.col_vector(1)))

    print("{} + {} = {}".format(matrix, matrix2, matrix + matrix2))

    print("{} - {} = {}".format(matrix, matrix2, matrix - matrix2))

    print("{} * {} = {}".format(matrix, 2, matrix * 2))

    print("{} * {} = {}".format(2, matrix, 2 * matrix))

    print("{} / {} = {}".format(matrix, 2, matrix / 2))


