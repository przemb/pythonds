from nose.tools import assert_equal, assert_true, assert_false, assert_raises
from stack import Stack


# check if input parentheses are balanced
def is_balanced(input_string):
    if not is_valid(input_string):
        raise ValueError

    tmp_stack = Stack()
    for ch in input_string:
        if ch in "([{":
            tmp_stack.push(ch)
        elif ch in ")]}":
            try:
                if not match(tmp_stack.pop(), ch):
                    return False
            except IndexError:
                return False

    return tmp_stack.empty()


def match(left_side, right_side):
    pairs = {")": "(",  "]": "[", "}": "{"}

    return pairs[right_side] == left_side


def is_valid(input_string):
    if type(input_string) != str:
        return False

    for ch in input_string:
        if ch not in "{}[]()":
            return False
    return True


assert_raises(ValueError, is_balanced, 1)
assert_true(is_balanced(""))
assert_false(is_balanced("((((((("))
assert_false(is_balanced("((()(()"))
assert_raises(ValueError, is_balanced, "() ()")
assert_false(is_balanced("))(("))
assert_true(is_balanced("(())()()"))
assert_true(is_balanced("({})[]()"))
assert_false(is_balanced("[()()[](}"))
assert_true(is_balanced("{[()()]}[]()"))