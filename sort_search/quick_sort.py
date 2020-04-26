from nose.tools import assert_equal
from random import randint


def quick_sort(container):
    """Quick sort - version mixed"""
    quick_sort_helper(container, 0, len(container)-1)


def quick_sort_helper(container, start_idx, end_idx):
    if start_idx < end_idx:
        partition_idx = partition(container, start_idx, end_idx)
        quick_sort_helper(container, start_idx, partition_idx-1)
        quick_sort_helper(container, partition_idx+1, end_idx)


def partition(container, start_idx, end_idx):
    pivot_idx = start_idx
    left_mark = start_idx + 1
    right_mark = end_idx

    while left_mark < right_mark:
        while container[left_mark] < container[pivot_idx]:
            left_mark += 1

        while container[right_mark] > container[pivot_idx]:
            right_mark -= 1

        if left_mark > right_mark:
            break
        container[left_mark], container[right_mark] = container[right_mark], container[left_mark]

    # final - swap pivot value with right_mark value
    container[pivot_idx], container[right_mark] = container[right_mark], container[pivot_idx]
    return right_mark  # return split point


lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(lst)
assert_equal([17, 20, 26, 31, 44, 54, 55, 77, 93], lst)

lst = []
quick_sort(lst)
assert_equal([], lst)

lst = [7, 5, 2, 11, 5, 1]
quick_sort(lst)
assert_equal([1, 2, 5, 5, 7, 11], lst)

lst = ['l', 'm', 'o', 'a']
quick_sort(lst)
assert_equal(['a', 'l', 'm', 'o'], lst)


#############################################################################


def quick_sort_l(container):
    """Version with Lomuto partition scheme"""
    _quick_sort_l(container, 0, len(container)-1)


def partition_l(container, start_idx, end_idx):
    partition_idx = start_idx
    pivot_val = container[end_idx]
    for i in range(start_idx, end_idx):
        if container[i] < pivot_val:
            container[i], container[partition_idx] = container[partition_idx], container[i]
            partition_idx += 1
    container[partition_idx], container[end_idx] = container[end_idx], container[partition_idx]
    return partition_idx


def _quick_sort_l(container, start_idx, end_idx):
    if start_idx < end_idx:
        choose_pivot_median_way(container, start_idx, end_idx)
        # choose_pivot_random_way(container, start_idx, end_idx)
        partition_idx = partition_l(container, start_idx, end_idx)
        _quick_sort_l(container, start_idx, partition_idx - 1)
        _quick_sort_l(container, partition_idx + 1, end_idx)


def choose_pivot_median_way(container, start_idx, end_idx):
    """Shuffle pivot - based on median"""
    mid_idx = (start_idx + end_idx) // 2
    if container[mid_idx] < container[start_idx]:
        container[mid_idx], container[start_idx] = container[start_idx], container[mid_idx]
    if container[end_idx] < container[start_idx]:
        container[end_idx], container[start_idx] = container[start_idx], container[end_idx]
    # final modification
    if container[mid_idx] < container[end_idx]:
        container[end_idx], container[mid_idx] = container[mid_idx], container[end_idx]


def choose_pivot_random_way(container, start_idx, end_idx):
    """Shuffle pivot - randomly"""
    new_pivot_idx = randint(start_idx, end_idx)
    container[end_idx], container[new_pivot_idx] = container[new_pivot_idx], container[end_idx]
    print(f"new pivot {new_pivot_idx}")


lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort_l(lst)
assert_equal([17, 20, 26, 31, 44, 54, 55, 77, 93], lst)

lst = []
quick_sort_l(lst)
assert_equal([], lst)

lst = [7, 5, 2, 11, 5, 1]
quick_sort_l(lst)
assert_equal([1, 2, 5, 5, 7, 11], lst)

lst = ['l', 'm', 'o', 'a']
quick_sort_l(lst)
assert_equal(['a', 'l', 'm', 'o'], lst)


#############################################################################

