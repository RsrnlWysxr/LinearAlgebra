import numpy as np

if __name__ == "__main__":

    print(np.__version__)

    # 生成向量
    vec = np.array([1, 2, 3])
    vec2 = np.array([3, 2, 1])
    zero = np.zeros(3)
    one = np.ones(4)
    four = np.full(3, 4)

    #  打印向量
    print(vec)
    print(vec2)
    print(vec[0])
    print(vec2[0])
    print(zero)
    print(one)
    print(four)

    # 运算
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(vec, 6, vec * 6))
    print("{} * {} = {}".format(6, vec, 6 * vec))
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2)))

    # 求模
    print("||{}|| = {}".format(vec, np.linalg.norm(vec)))
    # 单位向量
    print(vec / np.linalg.norm(vec))
    print(np.linalg.norm(vec / np.linalg.norm(vec)))