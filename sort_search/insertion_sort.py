from nose.tools import assert_equal


def insertion_sort(container):
    for i in range(1, len(container)):
        target_val = container[i]
        target_pos = i

        while container[target_pos-1] > target_val and target_pos > 0:
            container[target_pos] = container[target_pos-1]
            target_pos = target_pos - 1

        container[target_pos] = target_val
    return container


assert_equal([1, 2, 5, 5, 7, 11], insertion_sort([7, 5, 2, 11, 5, 1]))
assert_equal([], insertion_sort([]))
assert_equal(['a', 'l', 'm', 'o'], insertion_sort(['l', 'm', 'o', 'a']))
assert_equal([1, 2, 5, 5, 7, 11], insertion_sort([1, 2, 5, 5, 7, 11]))

