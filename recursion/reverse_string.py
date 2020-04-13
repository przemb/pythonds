from nose.tools import assert_equal, assert_true, assert_false, assert_raises, assert_not_equal


def reverse_string(word):
    if type(word) != str:
        raise TypeError

    if len(word) <= 1:
        return word
    else:
        return reverse_string(word[1:]) + word[0]


def is_palindrome(input_):
    if type(input_) != str:
        raise TypeError
    input_ = input_.replace(" ", "")
    input_ = input_.lower()
    return input_ == reverse_string(input_)


assert_equal("esroh", reverse_string("horse"))
assert_equal("", reverse_string(""))
assert_equal("spom", reverse_string("mops"))
assert_not_equal("cat", reverse_string("dog"))

assert_false(is_palindrome("cat"))
assert_true(is_palindrome(""))
assert_true(is_palindrome("kayak"))
assert_true(is_palindrome("Live not on evil"))
assert_false(is_palindrome("Wassamassaw – a town in South Dakota"))


