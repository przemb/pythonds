from nose.tools import assert_true, assert_false


class BinarySearch:
    def __init__(self, *args):
        self.list = [*args]
        self.list.sort()

    def __repr__(self):
        return str(self.list)

    def search(self, item):
        start = 0
        end = len(self.list) - 1
        while start <= end:
            midpoint = (start + end) // 2
            if item == self.list[midpoint]:
                return True
            elif item > midpoint:
                start = midpoint + 1
            else:  # item < midpoint:
                end = midpoint - 1
        return False

    def search_rec(self, item, start, end):
        if start > end:
            return False
        else:
            midpoint = (start + end) // 2
            if item == self.list[midpoint]:
                return True
            elif item > midpoint:
                start = midpoint + 1
                return self.search_rec(item, start, end)
            else:  # item < midpoint
                end = midpoint - 1
                return self.search_rec(item, start, end)


# iter
s = BinarySearch(5, 2, 9, 1, 3, 7)
assert_true(s.search(2))
s = BinarySearch(5, 2, 9, 1, 3, 7)
assert_false(s.search(12))
s = BinarySearch(5, 2, 9, 1, 3)
assert_true(s.search(3))
s = BinarySearch(5, 2, 9, 1, 3)
assert_false(s.search(17))

# rec
s = BinarySearch(5, 2, 9, 1, 3, 7)
assert_true(s.search_rec(2, 0, len(s.list)-1))
s = BinarySearch(5, 2, 9, 1, 3, 7)
assert_false(s.search_rec(12, 0, len(s.list)-1))
s = BinarySearch(5, 2, 9, 1, 3)
assert_true(s.search_rec(3, 0, len(s.list)-1))
s = BinarySearch(5, 2, 9, 1, 3)
assert_false(s.search_rec(17, 0, len(s.list)-1))
