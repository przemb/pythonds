from nose.tools import assert_equal
from random import randint


def quick_sort_l(container):
    """Quick sort - version with Lomuto partition scheme"""
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


def _test_partition_l():
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    partition_l(lst, 0, len(lst)-1)
    assert_equal([17, 20, 93, 54, 77, 31, 44, 55, 26], lst)

    lst = [7, 2, 1, 6, 8, 5, 3, 4]
    partition_l(lst, 0, len(lst)-1)
    assert_equal([2, 1, 3, 4, 8, 5, 7, 6], lst)


def _test_quick_sort_l():
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


if __name__ == "__main__":
    _test_partition_l()
    _test_quick_sort_l()

