from nose.tools import assert_equal

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
        self.get(item)

    def __delitem__(self, key):
        pass

    def __len__(self):
        return self.size

    def __contains__(self, item):
        pass

    def __iter__(self):
        pass

    def put(self, key, value):
        # check if tree has root
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self._put_r(self.root, key, value)
        self.size += 1

    def _put_r(self, current_node, new_key, new_value):

        if new_key < current_node.key:
            if current_node.has_left_child():
                self._put_r(current_node.left_child, new_key, new_value)
            else:
                current_node.left_child = TreeNode(new_key, new_value, parent=current_node)

        elif new_key > current_node.key:
            if current_node.has_right_child():
                self._put_r(current_node.right_child, new_key, new_value)
            else:
                current_node.right_child = TreeNode(new_key, new_value, parent=current_node)

    def get(self, key):
        pass


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

    def update_node_data(self, key, value, left_child, right_child):
        self.key = key
        self.value = value
        if self.has_left_child():
            self.left_child = left_child
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child = right_child
            self.right_child.parent = self
