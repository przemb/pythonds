from nose.tools import assert_true, assert_false, assert_equal, assert_raises
from doubly_linked_list import Node, DoublyLinkedList


class OrderedLinkedList(DoublyLinkedList):
    # add keeping ascending order
    def __init__(self):
        super(OrderedLinkedList, self).__init__()

    def _is_head(self, new):
        if new.get_data() < self.head.get_data():  # is it new head?
            new.set_next(self.head)
            self.head.set_prev(new)
            self.head = new
            return True

    def _is_tail(self, new):
        if new.get_data() > self.tail.get_data():  # is it new tail?
            self.tail.set_next(new)
            new.set_prev(self.tail)
            self.tail = new
            return True

    @staticmethod
    def _is_middle(new, current, next_):
        if current.get_data() < new.get_data() < next_.get_data():  # middle ?
            current.set_next(new)
            new.set_next(next_)
            next_.set_prev(new)
            new.set_prev(current)
            return True

    @staticmethod
    def _validate(elem):
        if type(elem) != int:
            raise TypeError

    def add(self, elem):
        self._validate(elem)
        new = Node(elem)
        if self.is_empty():
            self.head = new
            self.tail = new
        else:
            current = self.head
            next_ = current.get_next()
            while current is not None:
                if self._is_head(new) or self._is_tail(new) or self._is_middle(new, current, next_):
                    return True
                current = current.get_next()
                next_ = next_.get_next()
            return False

    def search(self, elem):
        current = self.head
        while current is not None and current.get_data() <= elem:
            if current.get_data() == elem:
                return True
            current = current.get_next()
        return False


def test_list():
    list_ = OrderedLinkedList()
    assert_true(list_.is_empty())
    assert_equal(0, list_.size())

    list_.add(7)
    assert_false(list_.is_empty())

    list_.add(5)
    assert_equal(2, list_.size())
    assert_false(list_.search(11))
    assert_raises(TypeError, list_.add, Node(3))
    assert_raises(TypeError, list_.add, 'a')

    list_.add(13)
    list_.add(11)
    assert_true(list_.search(5))
    assert_true(list_.search(13))
    assert_true(list_.search(7))
    assert_equal("Node(5) <-> Node(7) <-> Node(11) <-> Node(13) <-> ", str(list_))
    assert_equal(" <-> Node(13) <-> Node(11) <-> Node(7) <-> Node(5)", list_.get_reversed_repr())

    slice_list = list_.slice(0, 2)
    assert_equal("Node(5) -> Node(7) -> ", str(slice_list))
    slice_list = list_.slice(1, 4)
    assert_equal("Node(7) -> Node(11) -> Node(13) -> ", str(slice_list))

    list_.remove(7)
    assert_equal("Node(5) <-> Node(11) <-> Node(13) <-> ", str(list_))

    list_.remove(13)
    assert_equal("Node(5) <-> Node(11) <-> ", str(list_))
    assert_false(list_.remove(13))
    assert_equal("Node(5) <-> Node(11) <-> ", str(list_))

    list_.remove(5)
    assert_equal("Node(11) <-> ", str(list_))

    list_.add(1)
    assert_equal("Node(1) <-> Node(11) <-> ", str(list_))

    list_.add(12)
    assert_equal("Node(1) <-> Node(11) <-> Node(12) <-> ", str(list_))
    assert_equal(" <-> Node(12) <-> Node(11) <-> Node(1)", list_.get_reversed_repr())

    assert_equal(1, list_.index(11))
    assert_equal(0, list_.index(1))
    assert_equal(2, list_.index(12))
    assert_equal(False, list_.index(7))

    list_.add(0)
    list_.add(3)

    list_.pop()
    assert_equal("Node(0) <-> Node(1) <-> Node(3) <-> Node(11) <-> ", str(list_))
    assert_equal(" <-> Node(11) <-> Node(3) <-> Node(1) <-> Node(0)", list_.get_reversed_repr())

    list_.pop(0)
    assert_equal("Node(1) <-> Node(3) <-> Node(11) <-> ", str(list_))
    assert_equal(" <-> Node(11) <-> Node(3) <-> Node(1)", list_.get_reversed_repr())

    list_.pop(1)
    assert_equal("Node(1) <-> Node(11) <-> ", str(list_))
    assert_equal(" <-> Node(11) <-> Node(1)", list_.get_reversed_repr())
    assert_false(list_.pop(100))
    assert_equal(" <-> Node(11) <-> Node(1)", list_.get_reversed_repr())

    list_.remove(1)
    assert_equal(" <-> Node(11)", list_.get_reversed_repr())
    list_.remove(11)
    assert_equal("", str(list_))


if __name__ == "__main__":
    test_list()

