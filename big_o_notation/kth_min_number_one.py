from nose.tools import assert_equal, assert_raises

# O(nlogn) complexity

# get_kth_min_element
def get_kth_element(container, index):
    if index >= len(container):
        raise ValueError

    container.sort()
    return container[index]

a = [5, 4, 2, -1]
assert_raises(ValueError, get_kth_element, a, 4)
assert_equal(2, get_kth_element(a, 1) )
assert_equal(-1, get_kth_element(a, 0) )
