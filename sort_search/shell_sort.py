from nose.tools import assert_equal


def insertion_sort_mod(container, increment=1):
    for i in range(increment, len(container)):
        target_val = container[i]
        target_pos = i
        prev_pos = target_pos - increment

        while container[prev_pos] > target_val and prev_pos >= 0:
            container[target_pos] = container[prev_pos]
            target_pos = target_pos - increment
            prev_pos = prev_pos - increment

        container[target_pos] = target_val
    return container


assert_equal([1, 2, 5, 5, 7, 11], insertion_sort_mod([7, 5, 2, 11, 5, 1]))
assert_equal([], insertion_sort_mod([]))
assert_equal(['a', 'l', 'm', 'o'], insertion_sort_mod(['l', 'm', 'o', 'a']))
assert_equal([1, 2, 5, 5, 7, 11], insertion_sort_mod([1, 2, 5, 5, 7, 11]))
assert_equal([2, 1, 5, 5, 7, 11], insertion_sort_mod([7, 5, 2, 11, 5, 1], 2))
assert_equal([7, 5, 1, 11, 5, 2], insertion_sort_mod([11, 5, 2, 7, 5, 1], 3))
assert_equal([20, 26, 44, 17, 54, 31, 93, 55, 77], insertion_sort_mod([54, 26, 93, 17, 77, 31, 44, 55, 20], 4))
assert_equal([20, 17, 44, 26, 54, 31, 77, 55, 93], insertion_sort_mod([54, 26, 93, 17, 77, 31, 44, 55, 20], 2))
assert_equal([17, 20, 26, 31, 44, 54, 55, 77, 93], insertion_sort_mod([54, 26, 93, 17, 77, 31, 44, 55, 20], 1))


def shell_sort_min(container, increment=3):
    container = insertion_sort_mod(container, increment)
    container = insertion_sort_mod(container)
    return container


def shell_sort(container):
    """Version with variable number of increments"""
    increment = len(container) // 2

    while increment > 0:
        container = insertion_sort_mod(container, increment)
        print(f"after increment = {increment}, list looks {container}")
        increment = increment // 2

    return container


assert_equal([1, 2, 5, 5, 7, 11], shell_sort([7, 5, 2, 11, 5, 1]))
assert_equal([], shell_sort([]))
assert_equal(['a', 'l', 'm', 'o'], shell_sort(['l', 'm', 'o', 'a']))
assert_equal([1, 2, 5, 5, 7, 11], shell_sort([1, 2, 5, 5, 7, 11]))
assert_equal([17, 20, 26, 31, 44, 54, 55, 77, 93], shell_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))

