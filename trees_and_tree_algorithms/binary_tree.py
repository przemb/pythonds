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
        str_repr = "\n"

        for level, elems in self.draw_container.items():
            margin = '  ' * (width - level)
            missing_elem_margin = '   ' * (2 ** level - len(elems))
            str_repr += missing_elem_margin
            for elem in elems:
                str_repr += margin + str(elem)
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

    def preorder(self):
        self._preorder_r()
        print()

    def _preorder_r(self):
        print(self.root, end=' ')
        if self.left_child:
            self.left_child._preorder_r()
        if self.right_child:
            self.right_child._preorder_r()

    def preorder_str(self):
        return self._preorder_str_r(self)

    def _preorder_str_r(self, tree):
        if tree.left_child is None and tree.right_child is None:
            return f"{tree.root}"
        else:
            result = f"{tree.get_root_value()}"
            if tree.left_child:
                result += f" {self._preorder_str_r(tree.left_child)}"
            if tree.right_child:
                result += f" {self._preorder_str_r(tree.right_child)}"
            return result

    def postorder(self):
        self._postorder_r()
        print()

    def _postorder_r(self):
        if self.left_child:
            self.left_child._postorder_r()
        if self.right_child:
            self.right_child._postorder_r()
        print(self.root, end=' ')

    def postortder_str(self):
        return self._postorder_str_r(self)

    def _postorder_str_r(self, tree):
        if tree.left_child is None and tree.right_child is None:
            return f"{tree.root}"
        else:
            result = ""
            if tree.left_child:
                result += f"{self._postorder_str_r(tree.left_child)} "
            if tree.right_child:
                result += f"{self._postorder_str_r(tree.right_child)} "
            result += f"{tree.get_root_value()}"
            return result

    def inorder(self):
        self._inorder_r()
        print()

    def _inorder_r(self):
        if self.left_child:
            self.left_child._inorder_r()
        print(self.root, end=' ')
        if self.right_child:
            self.right_child._inorder_r()

    def inorder_str(self):
        return self._inorder_str_r(self)

    def _inorder_str_r(self, tree):
        if tree.left_child is None and tree.right_child is None:
            return f"{tree.root}"
        else:
            result = ""
            if tree.left_child:
                result += f"{self._inorder_str_r(tree.left_child)} "
            result += f"{tree.get_root_value()} "
            if tree.right_child:
                result += f"{self._inorder_str_r(tree.right_child)}"
            return result



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
    exp = "\n      a\n    b    c\n     d  e  f\n"
    assert_equal(exp, str(tree))

    # human friendly form:
    #      a
    #    b    c
    #     d  e  f

    print(tree)
    assert_equal("a b d c e f", tree.preorder_str())
    assert_equal("d b e f c a", tree.postortder_str())
    assert_equal("b d a e c f", tree.inorder_str())


if __name__ == "__main__":
    main()
