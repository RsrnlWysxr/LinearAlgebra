import math
from ._globals import is_zero, is_equal


class Vector:

    def __init__(self, lst):
        self._values = list(lst)    # 传入lst引用，使用list方法防止外部改变

    @classmethod
    def zero(cls, dim):
        """返回dim纬的零向量"""
        return Vector([0] * dim)

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e ** 2 for e in self._values))

    def normalize(self):
        """返回向量的单位向量"""
        if is_zero(self.norm()):
            raise ZeroDivisionError("Normalize error! Norm is zero.")
        return Vector(self / self.norm())

    def dot(self, other):
        assert len(self) == len(other), \
            "Error in product, Length of vectors must be same"
        return sum(a * b for a, b in zip(self, other))

    def underlying_list(self):
        """返回原先列表的拷贝"""
        return self._values[:]

    def __add__(self, other):
        """向量加法，返回结果向量"""
        assert len(self) == len(other), \
            "Error in adding, Length of vectors must be same"
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        """向量减法，返回结果向量"""
        assert len(self) == len(other), \
            "Error in subtracting, Length of vectors must be same"
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, k):
        """向量数量乘法，右乘法，k * self"""
        return Vector([k * e for e in self._values])

    def __rmul__(self, k):
        """向量数量乘法，左乘，self * k"""
        return self * k

    def __truediv__(self, k):
        """向量数量除法，self / k"""
        return (1 / k) * self

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1 * self

    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1 * self

    def __eq__(self, other):
        """返回两个向量是否相等"""
        other_list = other.underlying_list()
        if len(self._values) != len(other_list):
            return False
        return all(is_equal(x, y) for x, y in zip(self._values, other_list))

    def __ne__(self, other):
        """返回两个向量是否不等"""
        return not (self == other)

    def __iter__(self):
        """迭代器，支持for循环，本质为list，返回list迭代器即可"""
        return self._values.__iter__()

    def __len__(self):
        """返回向量纬度"""
        return len(self._values)

    def __getitem__(self, index):
        """取向量第index个元素"""
        return self._values[index]

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))

    def __repr__(self):
        return "Vector({})".format(self._values)
