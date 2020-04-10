from nose.tools import assert_equal, assert_true, assert_false, assert_raises
from stack import Stack


# check if input parentheses are balanced
def is_balanced(input_string):
    if type(input_string) != str:
        raise ValueError

    tmp_stack = Stack()
    for ch in input_string:
        if ch == "(":
            tmp_stack.push(ch)
        elif ch == ")":
            try:
                tmp_stack.pop()
            except IndexError:
                return False
        else:
            raise ValueError

    return tmp_stack.empty()


assert_raises(ValueError, is_balanced, 1)
assert_true(is_balanced(""))
assert_false(is_balanced("((((((("))
assert_false(is_balanced("((()(()"))
assert_raises(ValueError, is_balanced, "() ()")
assert_false(is_balanced("))(("))
assert_true(is_balanced("(())()()"))