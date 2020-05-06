from nose.tools import assert_equal, assert_raises, assert_true, assert_false
from collections import defaultdict

# note:
# previous MAP ADT:
# 1. binary search on list
# 2. search on hash table
# 3. binary search on trees  <------
# BST property: keys less then parent are in left subtree, key greater than parent are in right subtree


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.draw_container = defaultdict(list)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __delitem__(self, key):
        self.delete(key)

    def __len__(self):
        return self.size

    def __contains__(self, item):
        return self.get(item) is not None

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        self._validate(key)
        # check if tree has root
        if self.root is None:
            self.root = TreeNode(key, value)
            self.size += 1
        else:
            self._put_r(self.root, key, value)

    def _put_r(self, current_node, new_key, new_value):
        if new_key < current_node.key:
            if current_node.has_left_child():
                self._put_r(current_node.left_child, new_key, new_value)
            else:
                current_node.left_child = TreeNode(new_key, new_value, parent=current_node)
                self.size += 1

        elif new_key > current_node.key:
            if current_node.has_right_child():
                self._put_r(current_node.right_child, new_key, new_value)
            else:
                current_node.right_child = TreeNode(new_key, new_value, parent=current_node)
                self.size += 1

    def get(self, key, default=None):
        self._validate(key)
        if self.root is None:
            return default
        else:
            target_node = self._get_r(self.root, key)
            if target_node:
                return target_node.value
            else:
                return default

    def _get_r(self, current_node, key):
        if current_node is None:
            return None
        elif current_node.key == key:
            return current_node
        else:
            if key < current_node.key:
                return self._get_r(current_node.left_child, key)
            elif key > current_node.key:
                return self._get_r(current_node.right_child, key)

    @staticmethod
    def _validate(key):
        if type(key) is not int and type(key) is not float:
            raise TypeError

    def delete(self, key):
        if len(self) > 0:
            target_node = self._get_r(self.root, key)
            self._delete_target_node(target_node)
        else:
            self._node_not_found()

    def _delete_target_node(self, target_node):
        if target_node is None:
            self._node_not_found()
        elif target_node.is_root() and len(self) == 1:  # 0. one elem list?
            self._delete_root()
        elif target_node.is_leaf():                     # 1. no nodes!
            self._delete_v_leaf(target_node)
        elif target_node.has_both_children():           # 2. both children
            self._delete_v_both_children(target_node)
        else:                                           # 3. single child
            self._delete_v_single_child(target_node)
        return True

    def _node_not_found(self):
        raise KeyError('Key not found in the tree!')

    def _delete_root(self):
        """Delete root - when tree has one elem"""
        self.root = None
        self.size -= 1

    def _delete_v_leaf(self, target_node):
        """Delete node - variant with leaf"""
        if target_node.is_left_child():
            target_node.parent.left_child = None
        else:
            target_node.parent.right_child = None
        self.size -= 1

    def _delete_v_both_children(self, target_node):
        """Delete parent - variant with both children"""
        successor = target_node._find_successor()
        successor._disconnect_and_update()  # disconnect successor from previous family

        # "overwrite" target with successor data
        target_node.key = successor.key
        target_node.value = successor.value
        self.size -= 1

    def _delete_v_single_child(self, target_node):
        """Delete parent - variant with single child"""
        if target_node.has_left_child():
            self._delete_v_single_left_child_(target_node)
        else:
            self._delete_v_single_right_child(target_node)
        self.size -= 1

    @staticmethod
    def _delete_v_single_left_child_(target_node):
        if target_node.is_left_child():
            target_node.parent.left_child = target_node.left_child
            target_node.left_child.parent = target_node.parent

        elif target_node.is_right_child():
            target_node.parent.right_child = target_node.left_child
            target_node.left_child.parent = target_node.parent
        else:  # it must be a root!
            target_node.update_node_data(key=target_node.left_child.key,
                                         value=target_node.left_child.value,
                                         left_child=target_node.left_child.left_child,
                                         right_child=target_node.left_child.right_child)

    @staticmethod
    def _delete_v_single_right_child(target_node):
        if target_node.is_left_child():
            target_node.parent.left_child = target_node.right_child
            target_node.right_child.parent = target_node.parent

        elif target_node.is_right_child():
            target_node.parent.right_child = target_node.right_child
            target_node.right_child.parent = target_node.parent
        else:  # it must be a root!
            target_node.update_node_data(key=target_node.right_child.key,
                                         value=target_node.right_child.value,
                                         left_child=target_node.right_child.left_child,
                                         right_child=target_node.right_child.right_child)

    def prepare_parent_child_dict(self):
        """Create and return dict which presents relations between nodes:
        ret: {parent: [child1, child2], ...}
        """
        self.draw_container.clear()
        self.draw_container[0].append(self.root.key)
        self._prepare_parent_child_dict(self.root)

    def _prepare_parent_child_dict(self, tree):
        left_child = tree.left_child
        right_child = tree.right_child

        if left_child is None and right_child is None:  # base case
            return
        else:
            if left_child is not None:
                self.draw_container[tree.key].append(left_child.key)
                self._prepare_parent_child_dict(left_child)
            if right_child is not None:
                self.draw_container[tree.key].append(right_child.key)
                self._prepare_parent_child_dict(right_child)


class TreeNode:
    def __init__(self, key, value, left_child=None, right_child=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self.left_child is None and self.right_child is None

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def update_node_data(self, key, value, left_child, right_child):
        self.key = key
        self.value = value
        if self.has_left_child():
            self.left_child = left_child
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child = right_child
            self.right_child.parent = self

    def _find_successor(self):
        """Find successor which will replace target node.
        Successor:
        a) preserves relations between left child and right child of target node
        b) has no more than one child
        c) has the next largest key in the subtree
        """
        if self.has_right_child():
            return self.right_child._find_min_key()
        else:
            # not essential now, to do later
            return None

    def _find_min_key(self):
        """Iterate on the left branch to the leaf. The leaf has the min key!"""
        current_node = self
        while current_node.has_left_child():
            current_node = current_node.left_child
        return current_node

    def _disconnect_and_update(self):
        """Disconnect successor from other nodes, and  update new family relations"""
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        else:  # has one child
            if self.has_left_child():
                _child = self.left_child
            else:
                _child = self.right_child

            if self.is_left_child():
                self.parent.left_child = _child
            else:
                self.parent.right_child = _child
            _child.parent = self.parent

    def inorder(self):
        """Lets keep this method to better understand why I implemented below __iter__ in such way ;)"""
        self._inorder()
        print()

    def _inorder(self):
        if self.has_left_child():
            self.left_child._inorder()
        print(self.key, end=' ')
        if self.has_right_child():
            self.right_child._inorder()

    def __iter__(self):
        if self:
            if self.has_left_child():
                for node in self.left_child:
                    yield node
            yield self.key
            if self.has_right_child():
                for node in self.right_child:
                    yield node


def test_put():
    bst = BinarySearchTree()
    assert_equal(0, len(bst))
    bst.put(5, 'one')
    assert_equal(1, len(bst))
    bst.put(7, 'seven')
    bst.put(3, 'three')
    assert_equal(3, len(bst))

    assert_raises(TypeError, bst.put, 'a', 1)

    bst.put(3.3, 'three-three')
    assert_equal(4, len(bst))

    bst[9] = 'nine'
    assert_equal(5, len(bst))


def test_repeating_key():
    bst = BinarySearchTree()
    bst[9] = 'nine'
    assert_equal(1, len(bst))
    bst[9] = 'new_nine'
    assert_equal(1, len(bst))


def test_get():
    bst = BinarySearchTree()
    assert_raises(TypeError, bst.get, 'a')
    assert_equal(None, bst.get(7))
    assert_equal('lack of elem', bst.get(7, 'lack of elem'))

    bst.put(7, 'seven')
    bst.put(2, 'two')
    bst.put(9, 'nine')
    bst.put(1, 'one')
    bst.put(3, 'three')

    assert_equal('one', bst.get(1))
    assert_equal('three', bst[3])


def test_contains():
    bst = BinarySearchTree()
    bst[7] = 'seven'
    assert_true(7 in bst)
    assert_false(1 in bst)
    assert_raises(TypeError, bst.__contains__, 'a')


def test_delete_empty():
    bst = BinarySearchTree()
    assert_equal(0, len(bst))
    assert_raises(KeyError, bst.delete, 1)


def test_delete_root():
    bst = BinarySearchTree()
    bst[7] = 'seven'
    assert_raises(KeyError, bst.delete, 1)

    bst.delete(7)
    assert_equal(0, len(bst))
    assert_equal(None, bst.root)


def test_delete_leaf():
    bst = BinarySearchTree()
    bst[7] = 'seven'
    bst[6] = 'six'

    bst.delete(6)
    assert_equal(1, len(bst))
    assert_equal(7, bst.root.key)
    assert_equal(None, bst.root.left_child)


def test_del_keyword():
    bst = BinarySearchTree()
    bst[7] = 'seven'
    bst[6] = 'six'

    del bst[6]
    assert_equal(1, len(bst))
    assert_equal(7, bst.root.key)
    assert_equal(None, bst.root.left_child)


def test_delete_with_single_child_right():
    bst = BinarySearchTree()
    data = [17, 5, 25, 11, 2, 9, 16, 7, 35, 29, 38]
    for elem in data:
        bst.put(elem, '')

    bst.prepare_parent_child_dict()
    assert_equal({0: [17], 17: [5, 25], 5: [2, 11], 11: [9, 16],
                  9: [7], 25: [35], 35: [29, 38]}, bst.draw_container)

    bst.delete(25)
    bst.prepare_parent_child_dict()
    assert_equal({0: [17], 17: [5, 35], 5: [2, 11], 11: [9, 16],
                  9: [7], 35: [29, 38]}, bst.draw_container)
    assert_equal(10, len(bst))


def test_delete_with_single_child_left():
    bst = BinarySearchTree()
    data = [17, 5, 25, 11, 2, 9, 16, 7, 35, 29, 38]
    for elem in data:
        bst.put(elem, '')

    bst.prepare_parent_child_dict()
    assert_equal({0: [17], 17: [5, 25], 5: [2, 11], 11: [9, 16],
                  9: [7], 25: [35], 35: [29, 38]}, bst.draw_container)

    bst.delete(9)
    bst.prepare_parent_child_dict()
    assert_equal({0: [17], 17: [5, 25], 5: [2, 11], 11: [7, 16],
                  25: [35], 35: [29, 38]}, bst.draw_container)
    assert_equal(10, len(bst))


def test_delete_with_single_child_root():
    bst = BinarySearchTree()
    data = [17, 25, 35, 29, 38]
    for elem in data:
        bst.put(elem, '')

    bst.prepare_parent_child_dict()
    assert_equal({0: [17], 17: [25], 25: [35], 35: [29, 38]}, bst.draw_container)

    bst.delete(17)
    bst.prepare_parent_child_dict()
    assert_equal({0: [25], 25: [35], 35: [29, 38]}, bst.draw_container)
    assert_equal(4, len(bst))


def test_delete_with_two_children():
    bst = BinarySearchTree()
    data = [17, 5, 11, 2, 9, 16, 7, 35, 8, 29, 38]
    for elem in data:
        bst.put(elem, '')
    bst.prepare_parent_child_dict()
    assert_equal({0: [17], 17: [5, 35], 5: [2, 11], 11: [9, 16],
                  9: [7], 7: [8], 35: [29, 38]}, bst.draw_container)

    bst.delete(5)
    bst.prepare_parent_child_dict()
    assert_equal({0: [17], 17: [7, 35], 7: [2, 11], 11: [9, 16],
                  9: [8], 35: [29, 38]}, bst.draw_container)

    del bst[35]
    bst.prepare_parent_child_dict()
    assert_equal({0: [17], 17: [7, 38], 7: [2, 11], 11: [9, 16],
                  9: [8], 38: [29]}, bst.draw_container)
    assert_equal(9, len(bst))


def test_delete_with_two_children_root():
    bst = BinarySearchTree()
    data = [17, 5, 11, 2, 9, 16, 7, 35, 8, 29, 38]
    for elem in data:
        bst.put(elem, '')
    bst.prepare_parent_child_dict()
    assert_equal({0: [17], 17: [5, 35], 5: [2, 11], 11: [9, 16],
                  9: [7], 7: [8], 35: [29, 38]}, bst.draw_container)

    del bst[17]
    bst.prepare_parent_child_dict()
    assert_equal({0: [29], 29: [5, 35], 5: [2, 11], 11: [9, 16],
                  9: [7], 7: [8], 35: [38]}, bst.draw_container)
    assert_equal(29, bst.root.key)
    assert_equal(10, len(bst))


def test_iterator():
    bst = BinarySearchTree()
    data = [17, 5, 11, 2, 9, 16, 7, 35, 8, 29, 38]
    for elem in data:
        bst.put(elem, '')

    assert_equal([2, 5, 7, 8, 9, 11, 16, 17, 29, 35, 38], list(iter(bst)))


if __name__ == "__main__":
    test_put()
    test_get()
    test_repeating_key()
    test_contains()
    test_delete_empty()
    test_delete_root()
    test_delete_leaf()
    test_del_keyword()
    test_delete_with_single_child_right()
    test_delete_with_single_child_left()
    test_delete_with_single_child_root()
    test_delete_with_two_children()
    test_delete_with_two_children_root()
    test_iterator()
