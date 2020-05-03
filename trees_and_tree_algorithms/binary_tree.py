from nose.tools import assert_equal
from collections import defaultdict


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None
        self.draw_container = defaultdict(list)

    def __repr__(self):
        return self.prepare_drawing()

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

    def prepare_drawing(self):
        if len(self.draw_container) == 0:
            self.draw_container[0].append(self.root)
            self._prepare_drawing(self, 0)

        width = len(self.draw_container)
        str_repr = ""

        for level, elems in self.draw_container.items():
            margin = '  ' * (width - level)
            missing_elem_margin = '   ' * (2 ** level - len(elems))
            str_repr += missing_elem_margin
            for elem in elems:
                str_repr += margin + str(elem)
            str_repr += '\n'
        str_repr += '\n'
        return str_repr

    def _prepare_drawing(self, tree, level):
        left_child = tree.get_left_child()
        right_child = tree.get_right_child()

        level += 1
        # print(f"level: {level}")

        if left_child is None and right_child is None:  # base case
            return
        else:
            if left_child is not None:
                self.draw_container[level].append(left_child.root)
                self._prepare_drawing(left_child, level)
            if right_child is not None:
                self.draw_container[level].append(right_child.root)
                self._prepare_drawing(right_child, level)


def build_tree():
    r = BinaryTree('a')
    r.insert_left('b')
    r.insert_right('c')
    r.get_left_child().insert_right('d')
    r.get_right_child().insert_left('e')
    r.get_right_child().insert_right('f')
    return r


def main():
    tree = build_tree()
    assert_equal('c', tree.get_right_child().get_root_value())
    assert_equal('d', tree.get_left_child().get_right_child().get_root_value())
    assert_equal('e', tree.get_right_child().get_left_child().get_root_value())

    # test visual repr
    exp = "      a\n    b    c\n     d  e  f\n\n"
    assert_equal(exp, str(tree))

    # human friendly form:
    #      a
    #    b    c
    #     d  e  f

    print(tree)


if __name__ == "__main__":
    main()
