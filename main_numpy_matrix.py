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

    # 单位矩阵
    I = np.identity(2)
    print("T.dot(I) = \n{}".format(T.dot(I)))
    print("I.dot(T) = \n{}".format(I.dot(T)))

    # 逆矩阵
    invA = np.linalg.inv(T)
    print(invA)
    print(invA.dot(T))
    print(T.dot(invA))