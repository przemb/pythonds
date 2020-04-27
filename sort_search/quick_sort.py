from nose.tools import assert_equal
from quick_sort_l import choose_pivot_median_way


def quick_sort(container):
    """Quick sort - version mixed"""
    quick_sort_helper(container, 0, len(container)-1)


def quick_sort_helper(container, start_idx, end_idx):
    if start_idx < end_idx:
        #choose_pivot_median_way(container, start_idx, end_idx)
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


def _test_partition():
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    partition(lst, 0, len(lst)-1)
    assert_equal([31, 26, 20, 17, 44, 54, 77, 55, 93], lst)

    lst = [14, 17, 13, 15, 19, 10, 3, 16, 9, 12]
    partition(lst, 0, len(lst)-1)
    assert_equal([10, 12, 13, 9, 3, 14, 19, 16, 15, 17], lst)


def _test_quick_sort():
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


if __name__ == "__main__":
    _test_partition()
    _test_quick_sort()
