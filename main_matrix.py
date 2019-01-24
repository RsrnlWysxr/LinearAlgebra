from playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == '__main__':
    matrix = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])

    # print("{}".format(matrix))
    #
    # print(matrix.shape())
    #
    # print("matrix[0][1] = {}".format(matrix[0, 1]))
    #
    # print("matrix_row[1] = {}".format(matrix.row_vector(1)))
    #
    # print("matrix_col[1] = {}".format(matrix.col_vector(1)))
    #
    # print("{} + {} = {}".format(matrix, matrix2, matrix + matrix2))
    #
    # print("{} - {} = {}".format(matrix, matrix2, matrix - matrix2))
    #
    # print("{} * {} = {}".format(matrix, 2, matrix * 2))
    #
    # print("{} * {} = {}".format(2, matrix, 2 * matrix))
    #
    # print("{} / {} = {}".format(matrix, 2, matrix / 2))

    # T = Matrix([[1.5, 0], [0, 2]])
    # p = Vector([5, 3])
    # print("T.dot(p) = {}".format(T.dot(p)))
    # P = Matrix([[0, 4, 5], [0, 0, 3]])
    # print("T.dot(P) = {}".format(T.dot(P)))
    # print("P.T = {}".format(P.T()))
    #
    # zero2 = Matrix.zero(2,2)
    # print(zero2)

    I = Matrix.identity(2)
    print(I)
    print(matrix.dot(I))

