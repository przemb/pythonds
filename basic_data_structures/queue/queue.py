from nose.tools import assert_equal, assert_raises, assert_true, assert_false

class Queue:
    def __init__(self, *args):
        self.data = [*args[::-1]]

    def __repr__(self):
        return f"Queue({self.data})"

    def enque(self, item):  # O(n)
        self.data.insert(0, item)

    def deque(self):  # O(1)
        return self.data.pop()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.data)


def main():
    q = Queue()  # direction --->
    assert_true(q.is_empty())
    q.enque('a')
    assert_equal(1, q.size())
    q.enque('b')
    assert_equal(['b', 'a'], q.data)
    q.deque()
    assert_equal(['b'], q.data)

    q2 = Queue(1, 2, 4, 6)
    assert_equal([6, 4, 2, 1], q2.data)

if __name__ == "__main__":
    main()
