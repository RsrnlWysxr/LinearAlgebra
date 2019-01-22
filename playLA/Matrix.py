from .Vector import Vector

class Matrix:

    def __init__(self, lst2d):
        self._values = [row for row in lst2d]

    def row_index(self, index):
        """返回矩阵第index个行向量"""
        return Vector(self._values[index])

    def col_index(self, index):
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

    __len__ = col_index

    def __repr__(self):
        return "Matrix({})".format(self._values)

    def __str__(self):
        return "\n".join([str(row) for row in self._values])

    def __getitem__(self, pos):
        """返回矩阵pos位置的元素"""
        r, c = pos
        return self._values[r][c]
