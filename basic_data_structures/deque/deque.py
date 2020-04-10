from nose.tools import assert_equal

# pseudo implementation of deque
class Deque:
    def __init__(self, *args):
        self.data = [*args]

    def __repr__(self):
        return f'Deque({self.data})'

    def append(self, item):
        self.data.append(item)

    def append_left(self, item):
        self.data.insert(0, item)

    def pop(self):
        return self.data.pop()

    def pop_left(self):
        return self.data.pop(0)

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0


def main():
    d = Deque(1, 2, 4)
    assert_equal(3, d.size())
    d.append(5)
    assert_equal([1, 2, 4, 5], d.data)
    d.append_left(9)
    assert_equal([9, 1, 2, 4, 5], d.data)
    d.pop_left()
    assert_equal([1, 2, 4, 5], d.data)
    d.pop()
    assert_equal([1, 2, 4], d.data)


if __name__ == "__main__":
    main()
