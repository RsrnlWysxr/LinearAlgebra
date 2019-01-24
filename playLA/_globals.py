EPSILON = 1e-8

def is_zero(x):
    return x < EPSILON

def is_equal(a, b):
    return (a - b) < EPSILON