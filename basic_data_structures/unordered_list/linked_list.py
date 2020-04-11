from nose.tools import assert_true, assert_false, assert_equal, assert_raises


class Node:
    def __init__(self, init_data):
        self._data = init_data
        self._next = None

    def __repr__(self):
        return f"Node({self._data})"

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, next_):
        self._next = next_


# singly linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        repr_str = ""
        current = self.head
        while current is not None:
            repr_str = repr_str + str(current) + " -> "
            current = current.get_next()
        return repr_str

    def is_empty(self):
        return self.head is None

    # add at the beginning
    def add(self, item):
        if type(item) == Node:
            raise TypeError

        new = Node(item)
        new.set_next(self.head)
        self.head = new

    def size(self):
        counter = 0
        current = self.head
        while current is not None:
            current = current.get_next()
            counter = counter + 1
        return counter

    # is it elem on the list?
    def search(self, elem):
        current = self.head
        while current is not None:
            if current.get_data() == elem:
                return True
            current = current.get_next()
        return False

    def remove(self, elem):
        previous = None
        current = self.head
        while current is not None:
            if current.get_data() == elem:
                continuation = current.get_next()
                del current
                if previous is not None:
                    previous.set_next(continuation)
                else:
                    self.head = continuation
                return True
            previous = current
            current = current.get_next()
        return False

    def append(self, element):
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        new = Node(element)
        current.set_next(new)

    def index(self, element):
        counter = 0
        current = self.head
        while current is not None:
            if current.get_data() == element:
                return counter

            current = current.get_next()
            counter = counter + 1
        return False

    def insert(self, position, element):
        if position == 0:
            return self.add(element)
        current = self.head
        counter = 0
        while current is not None:
            if counter + 1 == position:
                continuation = current.get_next()
                new = Node(element)
                new.set_next(continuation)
                current.set_next(new)
                return True
            current = current.get_next()
            counter = counter + 1
        return False

    def pop(self, position=None):
        current = self.head
        counter = 0
        previous = None
        if position is None:
            last_index = self.size()-1
            position = last_index

        while current is not None:
            if counter == position:
                if position == 0:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                del current
                return True
            previous = current
            current = current.get_next()
            counter = counter + 1
        return False


def test_list():
    list_ = SinglyLinkedList()
    assert_true(list_.is_empty())
    assert_equal(0, list_.size())
    list_.add(5)
    assert_false(list_.is_empty())
    list_.add(7)
    assert_equal(2, list_.size())
    assert_false(list_.search(11))
    assert_true(list_.search(5))
    assert_raises(TypeError, list_.add, Node(3))
    list_.add(11)
    list_.add(13)
    assert_equal("Node(13) -> Node(11) -> Node(7) -> Node(5) -> ", str(list_))
    list_.remove(7)
    assert_equal("Node(13) -> Node(11) -> Node(5) -> ", str(list_))
    list_.remove(13)
    assert_equal("Node(11) -> Node(5) -> ", str(list_))
    assert_false(list_.remove(13))
    assert_equal("Node(11) -> Node(5) -> ", str(list_))
    list_.remove(5)
    assert_equal("Node(11) -> ", str(list_))
    list_.append(1)
    assert_equal("Node(11) -> Node(1) -> ", str(list_))
    list_.append(12)
    assert_equal("Node(11) -> Node(1) -> Node(12) -> ", str(list_))
    assert_equal(0, list_.index(11))
    assert_equal(1, list_.index(1))
    assert_equal(2, list_.index(12))
    assert_equal(False, list_.index(7))
    list_.insert(0, "a")
    assert_equal("Node(a) -> Node(11) -> Node(1) -> Node(12) -> ", str(list_))
    list_.insert(2, "b")
    assert_equal("Node(a) -> Node(11) -> Node(b) -> Node(1) -> Node(12) -> ", str(list_))
    assert_false(list_.insert(100, "Y"))
    assert_equal("Node(a) -> Node(11) -> Node(b) -> Node(1) -> Node(12) -> ", str(list_))
    list_.pop()
    assert_equal("Node(a) -> Node(11) -> Node(b) -> Node(1) -> ", str(list_))
    list_.pop(0)
    assert_equal("Node(11) -> Node(b) -> Node(1) -> ", str(list_))
    list_.pop(1)
    assert_equal("Node(11) -> Node(1) -> ", str(list_))
    assert_false(list_.pop(100))


def test_node():
    n = Node(3)
    assert_equal('Node(3)', str(n))
    assert_equal(3, n.get_data())
    n.set_data(10)
    assert_equal('Node(10)', str(n))
    o = Node(5)
    n.set_next(o)
    assert_equal('Node(5)', str(n.get_next()))


if __name__ == "__main__":
    test_node()
    test_list()
