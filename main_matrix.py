from playLA.Matrix import Matrix

if __name__ == '__main__':
    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)

    print(matrix.shape())

    print("matrix[0][1] = {}".format(matrix[0, 1]))

    print("matrix_row[1] = {}".format(matrix.row_index(1)))

    print("matrix_col[1] = {}".format(matrix.col_index(1)))

