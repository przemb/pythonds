from nose.tools import assert_equal, assert_raises

def find_min(container):
    if len(container) < 1:
        raise ValueError

    min_num = container[0]
    for elem in container:
        for elem2 in container:
            if elem2 < elem:
                min_num = elem2
    return min_num

a = [1, 5, -2 , 10]
assert_equal(min(a), find_min(a))
b = []
assert_raises(ValueError, find_min, b)
c = [0, 0, -2, "a"]
assert_raises(TypeError, find_min, c)
d = [5, -4, 20, -7, 15, 11, 0, -2]
assert_equal(min(d), find_min(d))

