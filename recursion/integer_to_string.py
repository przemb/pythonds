from nose.tools import assert_equal, assert_not_equal, assert_raises

strings = "".join(str(i) for i in range(0, 10))
strings = strings + "ABCDEF"


def integer_to_string(num, base):
    if num < 0:
        raise ValueError

    # 796 -> "796"
    # 796 % 10 = 6
    # 796 // 10 = 79 <-
    # 79 % 10 = 9
    # 79 // 10 = 7 <-
    # 7 % 10 = 7
    if num < base:
        return strings[num]
    else:
        return integer_to_string(num // base, base) + strings[num % base]


assert_equal("796", integer_to_string(796, 10))
assert_equal("0", integer_to_string(0, 10))
assert_raises(ValueError, integer_to_string, -2, 10)
assert_equal("1010", integer_to_string(10, 2))
assert_equal("10", integer_to_string(16, 16))
assert_equal("FF", integer_to_string(255, 16))
assert_equal("11111111", integer_to_string(255, 2))
