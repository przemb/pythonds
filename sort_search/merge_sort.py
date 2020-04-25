from nose.tools import assert_equal


def merge_sort_slice(container):
    if len(container) <= 1:
        return container

    middle = len(container) // 2
    left = container[:middle]
    right = container[middle:]
    left = merge_sort_slice(left)
    right = merge_sort_slice(right)
    return merge_slice(container, left, right)


def merge_slice(container, left_half, right_half):
    i = 0; j = 0; k = 0;
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            container[k] = left_half[i]
            i += 1
        else:
            container[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        container[k] = left_half[i]
        k += 1
        i += 1

    while j < len(right_half):
        container[k] = right_half[j]
        k += 1
        j += 1

    return container


assert_equal([17, 20, 26, 31, 44, 54, 55, 77, 93], merge_sort_slice([54, 26, 93, 17, 77, 31, 44, 55, 20]))
assert_equal([], merge_sort_slice([]))

