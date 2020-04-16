from nose.tools import assert_equal


class ChangeProblem:
    _counter = 0

    def __init__(self):
        self.coinValueList = [1, 5, 10, 25]  # available coins
        self.known_results = {value: 1 for value in self.coinValueList}

    def get_min_n_coins(self, change):
        """Find minimum number of coins for given change"""
        ChangeProblem._counter += 1

        min_number_of_coins = change  # change x penny
        if change in self.known_results:
            return self.known_results[change]
        else:
            for value in self.coinValueList:
                if value <= change:
                    num_of_coins = 1 + self.get_min_n_coins(change - value)
                    if num_of_coins < min_number_of_coins:
                        min_number_of_coins = num_of_coins
            self.known_results[change] = min_number_of_coins
            return min_number_of_coins


change = ChangeProblem()
assert_equal(3, change.get_min_n_coins(7))
assert_equal(6, change.get_min_n_coins(63))  # 63 = 25 + 25 + 10 + 1 + 1 + 1
assert_equal(207, change._counter)  # check number of recursive calls


class ChangeProblemIter:
    def __init__(self):
        self.coinValueList = [1, 5, 10, 25]  # available coins
        self.known_results = {value: 1 for value in self.coinValueList}

    def get_min_n_coins(self, change):
        """Find minimum number of coins for given change"""

        for cents in range(change+1):
            min_number_of_coins = cents  # cents x penny
            for value in self.coinValueList:
                if value <= cents:
                    num_of_coins = 1 + self.known_results[cents - value]
                    if num_of_coins < min_number_of_coins:
                        min_number_of_coins = num_of_coins
            self.known_results[cents] = min_number_of_coins
        return self.known_results[change]



change_iter = ChangeProblemIter()
assert_equal(3, change_iter.get_min_n_coins(7))
assert_equal(6, change_iter.get_min_n_coins(63))  # 63 = 25 + 25 + 10 + 1 + 1 + 1

class ChangeProblemIntro:
    _counter = 0

    def __init__(self):
        self.coinValueList = [1, 5, 10, 25]
        self.known_results = {}

    def get_min_n_coins_toy(self, change):
        """Find minimum number of coins for given change"""
        ChangeProblemIntro._counter += 1

        min_number_of_coins = change  # change x penny
        if change in self.coinValueList:
            self.known_results[change] = 1
            return 1
        else:
            for value in self.coinValueList:
                if value <= change:
                    num_of_coins = 1 + self.get_min_n_coins_toy(change - value)
                    if num_of_coins < min_number_of_coins:
                        min_number_of_coins = num_of_coins
            return min_number_of_coins


change_problem = ChangeProblemIntro()
assert_equal(6, change_problem.get_min_n_coins_toy(63))
# assert_equal(67716925, change_problem._counter)


