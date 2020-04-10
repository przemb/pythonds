from nose.tools import assert_equal, assert_raises
from stack import Stack


# converts dec input to hex string
def dec_to_base(dec_input, target_base=2):
    validate(dec_input, target_base)
    tmp_stack = Stack()
    base_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
                 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L',
                 22: 'M', 23: 'N', 24: 'O', 25: 'P'}

    while dec_input != 0:
        reminder = dec_input % target_base
        if reminder > 9:
            tmp_stack.push(base_dict.get(reminder))
        else:
            tmp_stack.push(reminder)
        dec_input = dec_input // target_base
    return collect_result(tmp_stack, target_base)


def collect_result(tmp_stack, base):
    result_str = [str(tmp_stack.pop()) for i in range(0, tmp_stack.size())]
    literals = {2: '0b', 8: '0o', 16: '0x', 10: ''}

    result = literals.get(base, '0?') + ''.join(result_str)
    print(result)
    return result


def validate(dec_input, base):
    if type(dec_input) != int or dec_input < 0:
        raise ValueError


assert_raises(ValueError, dec_to_base, -1)
assert_raises(ValueError, dec_to_base, 'k')
assert_equal("0b11101001", dec_to_base(233))
assert_equal("0o351", dec_to_base(233, 8))
assert_equal("233", dec_to_base(233, 10))
assert_equal("0xE9", dec_to_base(233, 16))
assert_equal("0o31", dec_to_base(25, 8))
assert_equal("0x100", dec_to_base(256, 16))
assert_equal("0?10", dec_to_base(26, 26))