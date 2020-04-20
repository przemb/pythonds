from nose.tools import assert_equal, assert_true, assert_false


class SequentialSearch:
    def __init__(self, *args):
        self.list = [*args]

    def __repr__(self):
        return str(self.list)

    def search(self, item):
        for elem in self.list:
            if item == elem:
                return True
        return False


s = SequentialSearch(5, 2, 9, 1, 3)
assert_true(s.search(2))
assert_false(s.search(11))
