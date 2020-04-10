from nose.tools import assert_equal, assert_true, assert_false


class Stack:
    def __init__(self, *args):
        self.data = list(args)

    def __repr__(self):
        return f'Stack({self.data})'

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[len(self.data)-1]

    def empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


def main():
    s = Stack()
    assert_true(s.empty())
    assert_equal(s.size(), 0)
    s.push(4)
    assert_equal(s.size(), 1)
    s.push("h")
    assert_false(s.empty())
    assert_equal("h", s.pop())
    assert_equal([4], s.data)

    s = Stack(5, 2, 1)
    assert_equal([5, 2, 1], s.data)
    assert_equal(3, s.size())
    assert_equal(1, s.peek())
    assert_equal([5, 2, 1], s.data)
    assert_equal(3, s.size())


if __name__ == "__main__":
    main()

