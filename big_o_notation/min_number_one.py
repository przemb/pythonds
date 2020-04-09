from nose.tools import assert_equal, assert_raises

# O(n) complexity

def find_min(container):
    if (len(container) < 1):
        raise ValueError
    
    min_num = container[0]
    for item in container:
        if item < min_num:
            min_num = item
    return min_num

a = [6, 2, 5, 7, 1]
b = []
c = [-1, -100, 0, 5]

assert_equal(min(a), find_min(a))
assert_raises(ValueError, find_min, b)
assert_equal(min(c), find_min(c))
