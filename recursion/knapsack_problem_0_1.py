from nose.tools import assert_equal


class KnapsackIter:
    """Knapsack problem without repetitions - 0-1"""
    def __init__(self, input_weight=5, dict_={2: 3, 3: 4, 4: 8, 5: 6, 9: 10}):
        self.items_weight_value = dict_
        self.input_weight = input_weight
        self.saved_max_values = [
            [0 for w in range(self.input_weight + 1)] for i in range(len(self.items_weight_value) + 1)]

    def print_table(self):
        width = 2
        print("         ", end="")
        for i in range(self.input_weight+1):
            print(f"w{i} ", end="")
        print()
        for i in range(0, len(self.items_weight_value) + 1):
            print(f"item {i}:  ", end="")
            for w in range(0, self.input_weight + 1):
                print(f"{self.saved_max_values[i][w]:{width}}", end=" ")
            print()
        print()

    def find_max_value(self):
        input_weight = self.input_weight  # to simplify code...

        for i, (weight_i, value_i) in enumerate(self.items_weight_value.items(), start=1):
            for w in range(1, input_weight + 1):
                max_value = self.saved_max_values[i-1][w]
                if weight_i <= w:
                    tmp_value = value_i + self.saved_max_values[i-1][w - weight_i]
                    if tmp_value > max_value:
                        max_value = tmp_value
                self.saved_max_values[i][w] = max_value
                # k.print_table()
        return self.saved_max_values[len(self.items_weight_value)][input_weight]


k = KnapsackIter(5)
assert_equal(k.find_max_value(), 8)  # 6 vs 7 vs 8
k = KnapsackIter(6)
assert_equal(k.find_max_value(), 11)
k = KnapsackIter(8)
assert_equal(k.find_max_value(), 12) # 8 + 4
k = KnapsackIter(9)
assert_equal(k.find_max_value(), 15)  # 3 + 4 + 8
k = KnapsackIter(0)
assert_equal(k.find_max_value(), 0)
k = KnapsackIter(11)
assert_equal(k.find_max_value(), 17)  # 8 + 6 + 3

kpk = KnapsackIter(10, {6: 30, 3: 14, 4: 16, 2: 9})
assert_equal(kpk.find_max_value(), 46)

kpk = KnapsackIter(10, {5: 10, 4: 40, 6: 30, 3: 50})
assert_equal(kpk.find_max_value(), 90)


# why elms are not repeated?
# example:
# {2: 3, 3: 4, 4: 8, 5: 6, 9: 10}
# k = KnapsackIter(5)
# k.find_max_value()? # 6? vs 7? vs 8?
#  w[5][8] = ?
# w[4][8] = 12   vs    w[4][8 - 9] (invalid condition!)
# so:
# w[5][8] != 16             2 x {4: 8}
# w[5][8] = w[4][8] == 12       {3: 4, 4: 8}

