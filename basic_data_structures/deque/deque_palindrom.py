from nose.tools import assert_raises, assert_true, assert_false
from deque import Deque


def is_palindrome(input_str):
    input_str = validate(input_str)

    tmp_lst = list(input_str)
    tmp_deque = Deque(*tmp_lst)

    while tmp_deque.size() > 1:
        try:
            left_ch = tmp_deque.pop_left()
            right_ch = tmp_deque.pop()
        except IndexError:
            return False
        if left_ch != right_ch:
            return False

    if tmp_deque.size() == 1 or tmp_deque.size() == 0:
        return True


def validate(input_str):
    if type(input_str) != str:
        raise ValueError

    return input_str.replace(" ", "")

assert_raises(ValueError, is_palindrome, 1)
assert_true(is_palindrome("kayak"))
assert_false(is_palindrome("lemon"))
assert_true(is_palindrome(""))
assert_true(is_palindrome("radar"))
assert_true(is_palindrome("noon"))
assert_true(is_palindrome("madam im adam"))
