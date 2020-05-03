from nose.tools import assert_equal, assert_raises
from binary_tree import BinaryTree
from operator import add, sub, mul, truediv

# parse example input: (3 + (4 * 5))
# and save it as a tree

# algorithm - rules:
# 0. create root
# 1. if '(' - add add new node as a left child, move down, set current to left child
# 2. if number - fill current node and move up
# 3. if operator [-, +, /...] - fill current node, create right child, move down, set current to right child
# 4. if ')' - move up - current = parent


class ParseTree:
    def __init__(self, input_str):
        self.raw_input = input_str
        self.parsed_input = None
        self.tree = BinaryTree(None)
        self.parent_stack = []  # pseudo stack to keep track of current and parent
        self.current = self.tree

    def __repr__(self):
        return str(self.tree)

    def _parse_input(self):
        tmp = self.raw_input.replace(" ", "")
        self.parsed_input = list(tmp)

    def _process_left(self):
        self.current.insert_left(None)
        self.parent_stack.append(self.current)
        self.current = self.current.get_left_child()

    def _process_right(self):
        try:
            self.current = self.parent_stack.pop()
        except IndexError:
            pass

    def _process_operator(self, c):
        self.current.set_root_value(c)
        self.current.insert_right(None)
        self.parent_stack.append(self.current)
        self.current = self.current.get_right_child()

    def _process_number(self, c):
        self.current.set_root_value(int(c))
        self.current = self.parent_stack.pop()

    def run(self):
        self._parse_input()
        for c in self.parsed_input:
            if c == '(':
                self._process_left()
            elif c == ')':
                self._process_right()
            elif c in ['+', '-', '*', '/']:
                self._process_operator(c)
            else:
                self._process_number(c)

    def calculate(self):
        return self._calculate(self.tree)

    def _calculate(self, tree=None):
        left_child = tree.get_left_child()
        right_child = tree.get_right_child()

        if left_child is None and right_child is None:  # base case
            return tree.root
        else:
            operators = {'+': add, '-': sub, '*': mul, '/': truediv}

            operator_fn = operators[tree.get_root_value()]
            # simplified:
            # tmp = self._calculate(left_child) + self._calculate(right_child)
            tmp = operator_fn(self._calculate(left_child), self._calculate(right_child))
            return tmp

    def draw_dummy(self):
        """Dummy way to produce visual input. This method was replaced with prepare_drawing(),
        but lets keep if for edu purposes."""
        return self._draw_d(self.tree)

    def _draw_d(self, tree):
        left_child = tree.get_left_child()
        right_child = tree.get_right_child()

        if left_child is None and right_child is None:  # base case
            return f"{tree.root} "
        else:
            return f" {tree.get_root_value()}\n " \
                   f"{self._draw_d(left_child)} {self._draw_d(right_child)}\n"


if __name__ == "__main__":
    p = ParseTree("(3 + (4 * 5))")
    p._parse_input()
    assert_equal(['(', '3', '+', '(', '4', '*', '5', ')', ')'], p.parsed_input)

    p.run()
    assert_equal('+', p.tree.root)
    assert_equal(3, p.tree.get_left_child().root)
    assert_equal('*', p.tree.get_right_child().root)
    assert_equal(23, p.calculate())
    print(p)

    #      +
    #    3    *
    #        4  5

    p = ParseTree("((7 + 3) * (5 - 2))")
    p.run()
    assert_equal(30, p.calculate())
    print(p)

    #         *
    #       +    -
    #     7  3  5  2
