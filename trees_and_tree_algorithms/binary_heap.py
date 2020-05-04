from nose.tools import assert_equal, assert_true

# comment:
# inserting into list: O(n)
# sorting list: O(n log(n))
# BUT
# with BinaryHeap enqueue and dequeue is O(log(n)) !


class BinaryHeap:                   # p - parent, 2p - left child, 2p + 1 - right child
    def __init__(self):             # for node n, parent is n//2
        self.heap_list = [0]
        self.heap_size = 0

    def insert(self, item):
        """Add new item to the tree"""
        self.heap_list.append(item)
        self.heap_size += 1
        self._percolate_up(self.size())

    def _percolate_up(self, item_idx):
        """Traverse with item from bottom to the top and do as many swaps as needed"""
        n = item_idx
        item = self.heap_list[n]
        while n > 1:  # reorder
            parent = self.heap_list[n//2]
            if item < parent:
                self.heap_list[n//2], self.heap_list[n] = self.heap_list[n],  self.heap_list[n//2]
            n = n // 2

    def find_min(self):
        """Return the item with the minimum key value, leave item in the heap"""
        return self.heap_list[1]

    def del_min(self):
        """Return the item with the minimum key value, delete item from the heap"""
        if self.heap_size > 0:
            result = self.heap_list[1]

            new_root = self.heap_list.pop()
            self.heap_size -= 1

        if self.heap_size > 1:
            # update root
            self.heap_list[1] = new_root
            self._percolate_down(1)  # take first elem
        return result

    def _percolate_down(self, item_idx):
        n = item_idx
        elem = self.heap_list[n]
        while n < (self.heap_size - 1):
            child_idx = self._get_min_child_idx(n)
            if elem > self.heap_list[child_idx]:
                self.heap_list[n], self.heap_list[child_idx] = self.heap_list[child_idx], self.heap_list[n]
            n = n * 2

    def _get_min_child_idx(self, n):
        """
        :param n: node index
        """
        left = self.heap_list[2*n]
        if 2*n + 1 > self.size():
            return left
        else:
            if self.heap_list[2*n] < self.heap_list[2*n+1]:
                return 2*n
            else:
                return 2*n+1

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.heap_size

    def build_heap(self, list_of_keys):
        """Build tree using given list_of_keys"""
        self.heap_list += list_of_keys
        self.heap_size += len(list_of_keys)


def test_insert():
    b = BinaryHeap()
    b.build_heap([5, 9, 11, 14, 18, 19, 21, 33, 17, 27])
    b.insert(7)
    assert_equal([0, 5, 7, 11, 14, 9, 19, 21, 33, 17, 27, 18], b.heap_list)

    b = BinaryHeap()
    b.insert(7)
    assert_equal([0, 7], b.heap_list)


def test_del_min():
    b = BinaryHeap()
    b.build_heap([5, 9, 11, 14, 18, 19, 21, 33, 17, 27])
    tmp = b.del_min()
    assert_equal(5, tmp)
    assert_equal([0, 9, 14, 11, 17, 18, 19, 21, 33, 27], b.heap_list)

    b = BinaryHeap()
    b.build_heap([5])
    tmp = b.del_min()
    assert_equal(5, tmp)
    assert_equal([0], b.heap_list)
    assert_true(b.is_empty())


if __name__ == "__main__":
    test_insert()
    test_del_min()
