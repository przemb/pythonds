from nose.tools import assert_equal

# note:
# previous MAP ADT:
# 1. binary search on list
# 2. search on hash table
# 3. binary search on trees  <------


class BinarySearchTree:
    def __init__(self):
        pass

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        self.get(item)

    def __delitem__(self, key):
        pass

    def __len__(self):
        pass

    def __contains__(self, item):
        pass

    def put(self, key, value):
        pass

    def get(self, key):
        pass
