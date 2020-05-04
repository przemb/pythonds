from nose.tools import assert_equal

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
        self.percolate_up(item)

    def percolate_up(self, item):
        """Traverse with item from bottom to the top and do as many swaps as needed"""
        n = self.size()
        while n > 1:  # reorder
            parent = self.heap_list[n//2]
            if item < parent:
                self.heap_list[n//2], self.heap_list[n] = self.heap_list[n],  self.heap_list[n//2]
            n = n // 2

    def find_min(self):
        """Return the item with the minimum key value, leave item in the heap"""
        pass

    def del_min(self):
        """Return the item with the minimum key value, delete item from the heap"""
        pass

    def is_empty(self):
        pass

    def size(self):
        return self.heap_size

    def build_heap(self, list_of_keys):
        self.heap_list += list_of_keys
        self.heap_size += len(list_of_keys)


def test_insert():
    b = BinaryHeap()
    b.build_heap([5, 9, 11, 14, 18, 19, 21, 33, 17, 27])
    b.insert(7)
    assert_equal([0, 5, 7, 11, 14, 9, 19, 21, 33, 17, 27, 18], b.heap_list)


if __name__ == "__main__":
    test_insert()
