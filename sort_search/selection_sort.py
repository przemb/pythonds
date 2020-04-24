from nose.tools import  assert_equal


def selection_sort(container):
    for num_of_passes in range(len(container)-1, 0, -1):
        max_elem_index = 0
        for i in range(0, num_of_passes+1):
            if container[i] > container[max_elem_index]:
                max_elem_index = i

        if num_of_passes != max_elem_index:
            container[num_of_passes], container[max_elem_index] = container[max_elem_index], container[num_of_passes]
    return container


def selection_sort_lr(container):
    for num_of_passes in range(0, len(container)-1):
        min_index = num_of_passes
        for i in range(num_of_passes, len(container)):
            if container[i] < container[min_index]:
                min_index = i

        if num_of_passes != min_index:
            container[num_of_passes], container[min_index] = container[min_index], container[num_of_passes]
    return container


assert_equal([1, 2, 5, 5, 7, 11], selection_sort([7, 5, 2, 11, 5, 1]))
assert_equal([], selection_sort([]))
assert_equal(['a', 'l', 'm', 'o'], selection_sort(['l', 'm', 'o', 'a']))
assert_equal([1, 2, 5, 5, 7, 11], selection_sort([1, 2, 5, 5, 7, 11]))


assert_equal([1, 2, 5, 5, 7, 11], selection_sort_lr([7, 5, 2, 11, 5, 1]))
assert_equal([], selection_sort_lr([]))
assert_equal(['a', 'l', 'm', 'o'], selection_sort_lr(['l', 'm', 'o', 'a']))
assert_equal([1, 2, 5, 5, 7, 11], selection_sort_lr([1, 2, 5, 5, 7, 11]))
