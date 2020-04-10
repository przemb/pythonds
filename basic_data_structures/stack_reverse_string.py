from nose.tools import assert_equal, assert_raises


class Stack:
    def __init__(self, *args):
        self.data = list(args)

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def size(self):
        return len(self.data)


# simple reverse with toy stack data structure -> O(n)
def reverse_with_stack(string):
    if type(string) != str:
        raise ValueError

    tmp_input = list(string)
    tmp_stack = Stack(*tmp_input)
    tmp_list = [tmp_stack.pop() for x in range(0, tmp_stack.size())]
    return "".join(tmp_list)


assert_equal("tac", reverse_with_stack("cat"))
assert_equal("", reverse_with_stack(""))
assert_equal("x", reverse_with_stack("x"))
assert_raises(ValueError, reverse_with_stack, 1)
assert_equal("hsif", reverse_with_stack("fish"))