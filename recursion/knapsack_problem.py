from nose.tools import assert_equal


class KnapsackRec:
    """Knapsack problem with repetitions"""
    def __init__(self, dict_={2: 3, 3: 4, 4: 8, 5: 6, 9: 10}):
        self.items_weight_value = dict_
        self.saved_knowledge = {}

    def find_max_value(self, input_weight):
        max_value = 0
        if input_weight in self.saved_knowledge:
            return self.saved_knowledge[input_weight]
        else:
            for weight_i, value_i in self.items_weight_value.items():
                if weight_i <= input_weight:
                    tmp_value = value_i + self.find_max_value(input_weight - weight_i)
                    if tmp_value > max_value:
                        max_value = tmp_value
            self.saved_knowledge[input_weight] = max_value
            return max_value


assert_equal(KnapsackRec().find_max_value(5), 8)  # 5:(6) vs 2:3+3:4(7) vs 4:(8)
assert_equal(KnapsackRec().find_max_value(8), 16) # 2 x 8
assert_equal(KnapsackRec().find_max_value(0), 0)
assert_equal(KnapsackRec().find_max_value(11), 20)  # 13 vs 12 vs 20
assert_equal(KnapsackRec().find_max_value(9), 16)


class KnapsackIter:
    def __init__(self, dict_={2: 3, 3: 4, 4: 8, 5: 6, 9: 10}):
        self.items_weight_value = dict_
        self.saved_max_values = {}

    def find_max_value(self, input_weight):
        for w in range(input_weight + 1):
            max_value = 0
            for weight_i, value_i in self.items_weight_value.items():
                if weight_i <= w:
                    tmp_value = value_i + self.saved_max_values[w - weight_i]
                    if tmp_value > max_value:
                        max_value = tmp_value
            self.saved_max_values[w] = max_value
        return self.saved_max_values[input_weight]


assert_equal(KnapsackIter().find_max_value(5), 8)  # 6 vs 7 vs 8
assert_equal(KnapsackIter().find_max_value(6), 11)
assert_equal(KnapsackIter().find_max_value(8), 16)  # 8 + 8
assert_equal(KnapsackIter().find_max_value(9), 16)  # 8 + 8
assert_equal(KnapsackIter().find_max_value(0), 0)
assert_equal(KnapsackIter().find_max_value(11), 20)  # 13 vs 12 vs 20

assert_equal(KnapsackIter({6: 30, 3: 14, 4: 16, 2: 9}).find_max_value(10), 48)
assert_equal(KnapsackIter({5: 10, 4: 40, 6: 30, 3: 50}).find_max_value(10), 150)  # 3 x 50
