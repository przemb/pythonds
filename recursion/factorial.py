from nose.tools import assert_equal, assert_not_equal


# n! = n * (n-1)!
# 0! = 1
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)


assert_equal(1, factorial(0))
assert_equal(6, factorial(3))

