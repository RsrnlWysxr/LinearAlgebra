from playLA.Vector import Vector

if __name__ == "__main__":

    vec = Vector([5, 2])
    vec2 = Vector([2, 5])
    print(vec)
    print(len(vec))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))
    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(4, vec, 4 * vec))
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("-{} = {}".format(vec, -vec))
    print("+{} = {}".format(vec, +vec))

    zero2 = Vector.zero(2)
    print(zero2)

    print("normalize {} = {}".format(vec, vec.normalize()))
    print(vec.normalize().norm())

    try:
        zero2.normalize()
    except ZeroDivisionError:
        print("Cannot normalize zero vector {}.".format(zero2))

    print("{} . {} = {}".format(vec, vec2, vec.dot(vec2)))
