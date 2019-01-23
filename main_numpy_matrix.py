import numpy as np

if __name__ == '__main__':
    # 创建矩阵
    T = np.array([[1, 2], [3, 4]])
    print(T)

    # 获取矩阵元素
    print(T[:, 1])
    print(T[0])
    print(T[1, 1])

    # 矩阵加减法
    P = np.array([[3, 4], [5, 6]])
    print("{}".format(T + P))
    print("{}".format(T - P))

    # 矩阵数乘
    print("{}".format(T * P))
    print("{}".format(T * 3))
    print("{}".format(T / 3))

    # 矩阵点乘
    print("{}".format( T.dot(P)))