from nose.tools import assert_equal, assert_true, assert_false, assert_raises
from map_adt import Map


class Hash:
    def __init__(self, map_size):
        self.j = 0  # hash counter
        self.map_size = map_size  # const size
        self.max_limit = 2 * self.map_size

    def hash_function(self, key):
        result = (key + self.j**2) % self.map_size
        if self.j == self.max_limit:
            raise MemoryError

        self.j += 1
        return result


class MapQ(Map):
    """Variant of previous implementation with quadratic probing"""
    def _hash_function(self, key):
        raise AttributeError

    def _re_hash_function(self, oldhash):
        raise AttributeError

    def __delitem__(self, key):
        _h = Hash(self.size)
        hash_ = _h.hash_function(key)
        start_hash_ = hash_
        while self.slots[hash_] != key:
            hash_ = _h.hash_function(key)
            if hash_ == start_hash_:
                return False

        self.slots[hash_] = None
        self.data[hash_] = None
        return True

    def put(self, key, value):
        if len(self) == self.size:
            raise MemoryError

        _h = Hash(self.size)
        hash_ = _h.hash_function(key)

        if self.slots[hash_] is None:
            self.slots[hash_] = key
            self.data[hash_] = value
        else:
            if self.slots[hash_] == key:  # this key exists
                self.slots[hash_] = value  # overwrite
            else:
                new_hash = _h.hash_function(key)
                while self.slots[new_hash] is not None and self.slots[new_hash] != key:
                    new_hash = _h.hash_function(key)

                if self.slots[new_hash] is None:
                    self.slots[new_hash] = key
                    self.data[new_hash] = value
                else:
                    self.data[new_hash] = value  # overwrite

    def get(self, key, default=None):
        _h = Hash(self.size)
        hash_ = _h.hash_function(key)
        start_hash_ = hash_
        while self.slots[hash_] != key:
            hash_ = _h.hash_function(key)
            if hash_ == start_hash_:
                return default

        return self.data[hash_]


m = MapQ(3)
m.slots = ["a", "b", "c"]
m.data = [1, 2, 3]
assert_equal("{a: 1, b: 2, c: 3}", str(m))
assert_equal(3, len(m))

m = MapQ(3)
assert_equal("{None: None, None: None, None: None}", str(m))
assert_equal(0, len(m))

m = MapQ()
m[54] = "cat"; m[26] = "dog"; m[93] = "lion"; m[17] = "tiger"; m[77] = "bird";
m[31] = "cow"; m[44] = "goat"; m[55] = "pig";
m[20] = "chicken"
assert_equal("{77: bird, 44: goat, 20: chicken, 55: pig, 26: dog, 93: lion,"
             " 17: tiger, None: None, None: None, 31: cow, 54: cat}",
             str(m))

m[20] = "duck"

assert_equal("duck", m[20])
assert_equal(None, m[99])
assert_equal("replacement", m.get(99, "replacement"))

assert_true(20 in m)
assert_false(16 in m)
assert_true(54 in m)
assert_equal(9, len(m))
del m[20]
assert_equal(8, len(m))
assert_equal(None, m[20])

assert_raises(MemoryError, m[33], "fly")  # limitation of quadratic probing
# "there is no guarantee of finding an empty cell once the table becomes more than half full"
