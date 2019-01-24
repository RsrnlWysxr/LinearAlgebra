from .Vector import Vector

class Matrix:

    def __init__(self, lst2d):
        self._values = [row for row in lst2d]

    @classmethod
    def zero(cls, r, c):
        """返回一个r行c列的零矩阵"""
        return cls([[0] * c for _ in range(r)])

    @classmethod
    def identity(cls, n):
        """返回一个n行n列单位矩阵"""
        ret = [[0] * n for _ in range(n)]
        for i in range(n):
            ret[i][i] = 1
        return cls(ret)

    def size(self):
        """返回矩阵的元素个数"""
        r, c = self.shape()
        return r * c

    def row_vector(self, index):
        """返回矩阵第index个行向量"""
        return Vector(self._values[index])

    def col_vector(self, index):
        """返回矩阵第index个列向量"""
        return Vector([row[index] for row in self._values])

    def shape(self):
        """返回矩阵的形状:(行数,列数)"""
        return len(self._values), len(self._values[0])

    def row_num(self):
        """返回矩阵的行数"""
        return self.shape()[0]

    def col_num(self):
        """返回矩阵的列数"""
        return self.shape()[1]

    def dot(self, anther):
        """返回矩阵乘法的结果"""
        if isinstance(anther, Vector):
            # 与向量相乘
            assert self.col_num() == len(anther), \
                "Error in Matrix-Vector multiplication"
            return Vector([self.row_vector(i).dot(anther) for i in range(self.row_num())])
        if isinstance(anther, Matrix):
            # 与矩阵相乘
            assert self.col_num() == anther.row_num(), \
                "Error in Matrix-Matrix multiplication"
            return Matrix([[self.row_vector(i).dot(anther.col_vector(j)) for j in range(anther.col_num())]
                           for i in range(self.row_num())])

    def T(self):
        """返回矩阵的转置"""
        return Matrix([[e for e in self.col_vector(i)]
                       for i in range(self.col_num())])

    __len__ = row_num

    def __repr__(self):
        return "Matrix({})".format(self._values)

    # def __str__(self):
    #     return "\n".join([str(row) for row in self._values]) + '\n'

    __str__ = __repr__

    def __getitem__(self, pos):
        """返回矩阵pos位置的元素"""
        r, c = pos
        return self._values[r][c]

    def __add__(self, other):
        """返回两个矩阵的加法结果"""
        assert self.shape() == other.shape(), \
            "Error in adding, shape of Matrix must be same"
        return Matrix([[a + b for a, b in zip(self.row_vector(i), other.row_vector(i))]
                       for i in range(self.row_num())])

    def __sub__(self, other):
        """返回两个矩阵的减法结果"""
        assert self.shape() == other.shape(), \
            "Error in subtracting, shape of Matrix must be same"
        return Matrix([[a - b for a, b in zip(self.row_vector(i), other.row_vector(i))]
                       for i in range(self.row_num())])

    def __mul__(self, k):
        """返回矩阵数乘结果, self * k"""
        return Matrix([[e * k for e in self.row_vector(i)]
                       for i in range(self.row_num())])

    def __rmul__(self, k):
        """返回矩阵数乘结果, k * self"""
        return self * k

    def __truediv__(self, k):
        """返回矩阵除法结果, self / k"""
        return (1 / k) * self

    def __pos__(self):
        """返回矩阵取正结果"""
        return 1 * self

    def __neg__(self):
        """返回矩阵取负结果"""
        return -1 * self
