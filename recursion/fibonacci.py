from nose.tools import assert_equal, assert_raises


def fib_iter(n):
    counter = 0
    a, b = 0, 1
    while counter < n:
        yield a
        a, b = b, a+b
        counter += 1


def fib_iter_seq(n):
    result = []
    for elem in fib_iter(n):
        result.append(elem)
    return result


def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)


def fib_rec_seq(n):
    result = []
    for i in range(0, n):
        result.append(fib_rec(i))
    return result


assert_equal([], fib_iter_seq(-1))
assert_equal([0, 1, 1, 2, 3], fib_iter_seq(5))
assert_equal([0], fib_iter_seq(1))
assert_equal([], fib_rec_seq(-1))
assert_equal([0, 1, 1, 2, 3], fib_rec_seq(5))
assert_equal([0], fib_rec_seq(1))

