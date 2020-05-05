from nose.tools import assert_equal, assert_raises, assert_true, assert_false

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
        pass

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
        elif target_node.is_root() and len(self) == 1:  # 0. single root?
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
        return self._delete(target_node)

    def _delete_v_single_child(self, target_node):
        """Delete parent - variant with single child"""
        return self._delete(target_node)


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


def test_delete_magic():
    bst = BinarySearchTree()
    bst[7] = 'seven'
    bst[6] = 'six'

    del bst[6]
    assert_equal(1, len(bst))
    assert_equal(7, bst.root.key)
    assert_equal(None, bst.root.left_child)


if __name__ == "__main__":
    test_put()
    test_get()
    test_repeating_key()
    test_contains()
    test_delete_empty()
    test_delete_root()
    test_delete_leaf()
