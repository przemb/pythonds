from nose.tools import assert_equal


class Bubble:
    def __init__(self):
        self.counter = 0  # num of comparisons

    def bubble_sort(self, input_):
        for num_of_passes in range(len(input_)-1, 0, -1):
            for i in range(num_of_passes):
                self.counter += 1
                if input_[i] > input_[i+1]:
                    input_[i], input_[i+1] = input_[i+1], input_[i]
        return input_


b = Bubble()
assert_equal([1, 2, 5, 5, 7, 11], b.bubble_sort([7, 5, 2, 11, 5, 1]))
assert_equal([], b.bubble_sort([]))
assert_equal(['a', 'l', 'm', 'o'], b.bubble_sort(['l', 'm', 'o', 'a']))


class BubbleShort:
    def __init__(self):
        self.counter = 0  # num of comparisons

    def bubble_sort_short(self, input_):
        for num_of_passes in range(len(input_)-1, 0, -1):
            is_sorted = True
            for i in range(num_of_passes):
                self.counter += 1
                if input_[i] > input_[i+1]:
                    input_[i], input_[i+1] = input_[i+1], input_[i]
                    is_sorted = False
            if is_sorted:
                break
        return input_


bs = BubbleShort()
assert_equal([1, 2, 5, 5, 7, 11], bs.bubble_sort_short([7, 5, 2, 11, 5, 1]))
assert_equal([], bs.bubble_sort_short([]))
assert_equal(['a', 'l', 'm', 'o'], bs.bubble_sort_short(['l', 'm', 'o', 'a']))

b = Bubble()
assert_equal([1, 3, 4, 7, 8, 11], b.bubble_sort([1, 4, 3, 7, 8, 11]))
assert_equal(15, b.counter)

bs = BubbleShort()
assert_equal([1, 3, 4, 7, 8, 11], bs.bubble_sort_short([1, 4, 3, 7, 8, 11]))
assert_equal(9, bs.counter)