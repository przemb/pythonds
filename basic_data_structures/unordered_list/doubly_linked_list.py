from nose.tools import assert_true, assert_false, assert_equal, assert_raises
from linked_list import Node, SinglyLinkedList


class Node(Node):
    def __init__(self, init_data):
        self._data = init_data
        self._next = None
        self._prev = None

    def get_prev(self):
        return self._prev

    def set_prev(self, prev_):
        self._prev = prev_


# doubly linked list
class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        repr_str = ""
        current = self.head
        while current is not None:
            repr_str = repr_str + str(current) + " <-> "
            current = current.get_next()
        return repr_str

    def _update_internals_rem(self, previous, current):
        continuation = current.get_next()
        if previous is None:
            self.head = continuation
        else:
            previous.set_next(continuation)
        if continuation is None:
            self.tail = previous
        else:
            continuation.set_prev(previous)

    @staticmethod
    def _update_internals_ins(current, new):
        continuation = current.get_next()
        new.set_next(continuation)
        continuation.set_prev(new)
        current.set_next(new)
        new.set_prev(current)

    def get_reversed_repr(self):
        reversed_str = ""
        current = self.tail
        while current is not None:
            reversed_str = reversed_str + " <-> " + str(current)
            current = current.get_prev()
        return reversed_str

    # add at the beginning
    def add(self, item):
        if type(item) == Node:
            raise TypeError

        new = Node(item)
        if super(DoublyLinkedList, self).is_empty():
            self.tail = new
        else:
            new.set_next(self.head)
            self.head.set_prev(new)
        self.head = new

    def remove(self, elem):
        previous = None
        current = self.head
        while current is not None:
            if current.get_data() == elem:
                self._update_internals_rem(previous, current)
                del current
                return True
            previous = current
            current = current.get_next()
        return False

    # add at the end
    def append(self, element):
        tmp = self.tail
        new = Node(element)
        tmp.set_next(new)
        self.tail = new
        new.set_prev(tmp)

    def insert(self, position, element):
        if position == 0:
            return self.add(element)
        elif position == self.size() - 1:
            return self.append(element)
        current = self.head
        counter = 0
        while current is not None:
            if counter + 1 == position:
                new = Node(element)
                self._update_internals_ins(current, new)
                return True
            current = current.get_next()
            counter = counter + 1
        return False

    def pop(self, position=None):
        current = self.head
        counter = 0
        previous = None
        if position is None:
            position = self.size() - 1

        while current is not None:
            if counter == position:
                self._update_internals_rem(previous, current)
                del current
                return True
            previous = current
            current = current.get_next()
            counter = counter + 1
        return False


def test_list():
    list_ = DoublyLinkedList()
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
    assert_equal("Node(13) <-> Node(11) <-> Node(7) <-> Node(5) <-> ", str(list_))
    assert_equal(" <-> Node(5) <-> Node(7) <-> Node(11) <-> Node(13)", list_.get_reversed_repr())

    list_.remove(7)
    assert_equal("Node(13) <-> Node(11) <-> Node(5) <-> ", str(list_))

    list_.remove(13)
    assert_equal("Node(11) <-> Node(5) <-> ", str(list_))
    assert_false(list_.remove(13))
    assert_equal("Node(11) <-> Node(5) <-> ", str(list_))

    list_.remove(5)
    assert_equal("Node(11) <-> ", str(list_))

    list_.append(1)
    assert_equal("Node(11) <-> Node(1) <-> ", str(list_))

    list_.append(12)
    assert_equal("Node(11) <-> Node(1) <-> Node(12) <-> ", str(list_))
    assert_equal(" <-> Node(12) <-> Node(1) <-> Node(11)", list_.get_reversed_repr())

    assert_equal(0, list_.index(11))
    assert_equal(1, list_.index(1))
    assert_equal(2, list_.index(12))
    assert_equal(False, list_.index(7))

    list_.insert(0, "a")
    assert_equal("Node(a) <-> Node(11) <-> Node(1) <-> Node(12) <-> ", str(list_))
    assert_equal(" <-> Node(12) <-> Node(1) <-> Node(11) <-> Node(a)", list_.get_reversed_repr())

    list_.insert(2, "b")
    assert_equal("Node(a) <-> Node(11) <-> Node(b) <-> Node(1) <-> Node(12) <-> ", str(list_))
    assert_equal(" <-> Node(12) <-> Node(1) <-> Node(b) <-> Node(11) <-> Node(a)", list_.get_reversed_repr())
    assert_false(list_.insert(100, "Y"))
    assert_equal("Node(a) <-> Node(11) <-> Node(b) <-> Node(1) <-> Node(12) <-> ", str(list_))
    assert_equal(" <-> Node(12) <-> Node(1) <-> Node(b) <-> Node(11) <-> Node(a)", list_.get_reversed_repr())

    list_.pop()
    assert_equal("Node(a) <-> Node(11) <-> Node(b) <-> Node(1) <-> ", str(list_))
    assert_equal(" <-> Node(1) <-> Node(b) <-> Node(11) <-> Node(a)", list_.get_reversed_repr())

    list_.pop(0)
    assert_equal("Node(11) <-> Node(b) <-> Node(1) <-> ", str(list_))
    assert_equal(" <-> Node(1) <-> Node(b) <-> Node(11)", list_.get_reversed_repr())

    list_.pop(1)
    assert_equal("Node(11) <-> Node(1) <-> ", str(list_))
    assert_equal(" <-> Node(1) <-> Node(11)", list_.get_reversed_repr())
    assert_false(list_.pop(100))
    assert_equal(" <-> Node(1) <-> Node(11)", list_.get_reversed_repr())


def test_node():
    n = Node(3)
    assert_equal('Node(3)', str(n))
    assert_equal(3, n.get_data())
    n.set_data(10)
    assert_equal('Node(10)', str(n))
    n.set_next(Node(5))
    assert_equal('Node(5)', str(n.get_next()))
    n.set_prev(Node(2))
    assert_equal('Node(2)', str(n.get_prev()))


if __name__ == "__main__":
    # test_node()
    test_list()
