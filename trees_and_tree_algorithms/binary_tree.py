from nose.tools import assert_equal


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            tmp = BinaryTree()
            tmp.left_child = self.left_child  # move existing child one level down
            self.left_child = tmp

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            tmp = BinaryTree()
            tmp.right_child = self.right_child  # move existing child one level down
            self.right_child = tmp

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_value(self, value):
        self.root = value

    def get_root_value(self):
        return self.root


def build_tree():
    r = BinaryTree('a')
    r.insert_left('b')
    r.insert_right('c')
    r.get_left_child().insert_right('d')
    r.get_right_child().insert_left('e')
    r.get_right_child().insert_right('f')
    return r


tree = build_tree()
assert_equal('c', tree.get_right_child().get_root_value())
assert_equal('d', tree.get_left_child().get_right_child().get_root_value())
assert_equal('e', tree.get_right_child().get_left_child().get_root_value())
