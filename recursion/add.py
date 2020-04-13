from nose.tools import assert_equal, assert_not_equal


# recursive live sum
def list_sum(input_list):
    if len(input_list) == 1:
        return input_list[0]
    else:
        return input_list[0] + list_sum(input_list[1::])


assert_equal(5, list_sum([1, 2, 2]))
assert_not_equal(5, list_sum([0, 2, 2]))
