from nose.tools import assert_equal, assert_true, assert_false, assert_raises


class Map:
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size  # container with hashes
        self.data = [None] * self.size   # container with values

    def __repr__(self):
        str_repr = "{"
        for i in range(0, self.size):
            str_repr = str_repr + f"{self.slots[i]}: {self.data[i]}"
            if i != self.size - 1:
                str_repr = str_repr + ", "
        return str_repr + "}"

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __delitem__(self, key):
        hash_ = self._hash_function(key)
        start_hash_ = hash_
        while self.slots[hash_] != key:
            hash_ = self._re_hash_function(hash_)
            if hash_ == start_hash_:
                return False

        self.slots[hash_] = None
        self.data[hash_] = None
        return True

    def __len__(self):
        result = self.size
        for elem in self.slots:
            if elem is None:
                result = result - 1
        return result

    def __contains__(self, key):
        return self[key] is not None

    def _hash_function(self, key):
        return key % self.size

    def _re_hash_function(self, oldhash):  # linear probing
        return (oldhash + 1) % self.size

    def put(self, key, value):
        if len(self) == self.size:
            raise MemoryError

        hash_ = self._hash_function(key)

        if self.slots[hash_] is None:
            self.slots[hash_] = key
            self.data[hash_] = value
        else:
            if self.slots[hash_] == key:  # this key exists
                self.slots[hash_] = value  # overwrite
            else:
                new_hash = self._re_hash_function(hash_)
                while self.slots[new_hash] is not None and self.slots[new_hash] != key:
                    new_hash = self._re_hash_function(new_hash)

                if self.slots[new_hash] is None:
                    self.slots[new_hash] = key
                    self.data[new_hash] = value
                else:
                    self.data[new_hash] = value # overwrite

    def get(self, key, default=None):
        hash_ = self._hash_function(key)
        start_hash_ = hash_
        while self.slots[hash_] != key:
            hash_ = self._re_hash_function(hash_)
            if hash_ == start_hash_:
                return default

        return self.data[hash_]


m = Map(3)
m.slots = ["a", "b", "c"]
m.data = [1, 2, 3]
assert_equal("{a: 1, b: 2, c: 3}", str(m))
assert_equal(3, len(m))

m = Map(3)
assert_equal("{None: None, None: None, None: None}", str(m))
assert_equal(0, len(m))

m = Map()
m[54] = "cat"; m[26] = "dog"; m[93] = "lion"; m[17] = "tiger"; m[77] = "bird";
m[31] = "cow"; m[44] = "goat"; m[55] = "pig"; m[20] = "chicken"
assert_equal("{77: bird, 44: goat, 55: pig, 20: chicken, 26: dog, 93: lion, "
             "17: tiger, None: None, None: None, 31: cow, 54: cat}",
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
m[33] = "fly"; m[34] = "elephant"; m[35] = "giraffe";
assert_raises(MemoryError, m[36], "crocodile")
