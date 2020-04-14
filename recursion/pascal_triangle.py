from nose.tools import assert_equal, assert_raises
from math import factorial


class Triangle:
    def __init__(self, n):
        self.n = n  # number of rows
        self.data = self._prepare_data()

    def __repr__(self):
        return f"Triangle({self.n})"

    @staticmethod
    def binomial(n, k):
        #  nth row, kth elem
        if n < 0 or k < 0:
            raise ValueError
        if k == n:
            return 1
        else:
            return factorial(n) // (factorial(k) * factorial(n - k))

    def binomial_rec(self, n, k):
        #  nth row, kth elem
        if n < 0 or k < 0:
            return 0
        if k == n:
            return 1
        else:  # https://en.wikipedia.org/wiki/Binomial_coefficient
            return self.binomial_rec(n-1, k) + self.binomial_rec(n-1, k-1)

    def _prepare_data(self):
        row_data = {r: [] for r in range(0, self.n)}
        for n in range(0, self.n):
            for k in range(0, self.n):
                row_data[n].append(self.binomial_rec(n, k))
                if n == k:
                    break
        return row_data

    def draw(self):
        for i in range(0, self.n):
            space = " " * (self.n - 1 - i)
            for elem in self.data[i]:
                print(space + str(elem), end="")
                space = " "
            print()


t = Triangle(5)
assert_equal(1, t.binomial(0, 0))
assert_raises(ValueError, t.binomial, -1, 0)
assert_raises(ValueError, t.binomial, 0, 1)
assert_equal(1, t.binomial(1, 0))
assert_equal(1, t.binomial(2, 0))
assert_equal(2, t.binomial(2, 1))
assert_equal(15, t.binomial(6, 2))

t.draw()

