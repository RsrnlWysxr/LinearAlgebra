from .Matrix import Matrix
from .Vector import Vector
from ._globals import is_zero

class LinearSystem:

    def __init__(self, A, b):

        assert A.row_num() == len(b), \
            "row number of A must be equal to length of b"
        self._m = A.row_num()
        self._n = A.col_num()
        # 增广矩阵
        self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]])
                   for i in range(self._m)]
        # 记录主元列
        self.pivots = []

    def gauss_jordan_elimination(self):
        """有解,返回True/无解,返回False"""
        self._forward()
        self._backward()
        for i in range(len(self.pivots), self._m):
            if not is_zero(self.Ab[i][-1]):
                return False
        return True

    def _forward(self):

        i, k = 0, 0
        while i < self._m and k < self._n:
            # 看Ab[i][k]是否可以为主元
            max_row = self._max_row(i, k)
            # 交换两行
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]

            if is_zero(self.Ab[i][k]):
                k += 1
            else:
                # 归一
                self.Ab[i] = self.Ab[i] / self.Ab[i][k]
                for j in range(i + 1, self._m):
                    self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][k]
                self.pivots.append(k)
                i += 1

    def _max_row(self, index_i, index_j):
        """返回主元最大所在行号"""
        best, ret = self.Ab[index_i][index_j], index_i
        for i in range(index_i + 1, self._m):
            if self.Ab[i][index_j] > best:
                best, ret = self.Ab[i][index_j], i
        return ret

    def _backward(self):

        n = len(self.pivots)
        for i in range(n - 1, -1, -1):
            k = self.pivots[i]
            # A[i][k]为主元
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][k]

    def fancy_print(self):
        """打印结果"""
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=' ')
            print('|', self.Ab[i][-1])
