from nose.tools import assert_equal, assert_raises
from stack import Stack


def dec_to_bin(dec_input):
    validate(dec_input)
    tmp_stack = Stack()
    while dec_input != 0:
        reminder = dec_input % 2
        tmp_stack.push(reminder)
        dec_input = dec_input // 2
    return collect_result(tmp_stack)


def collect_result(tmp_stack):
    result_str = [tmp_stack.pop() for i in range(0, tmp_stack.size())]
    result = 0
    for power, value in enumerate(result_str):
        num = value * 10 ** (len(result_str) - 1 - power)  # separate digits to bin number
        result = result + num

    print(result)
    return result


def validate(dec_input):
    if type(dec_input) != int or dec_input < 0:
        raise ValueError


assert_raises(ValueError, dec_to_bin, -1)
assert_raises(ValueError, dec_to_bin, 'k')
assert_equal(11101001, dec_to_bin(233))
