from nose.tools import assert_true, assert_false

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    w1lst = list(word1)
    w2lst = list(word2)

    w1lst.sort()
    w2lst.sort()

    return "".join(w1lst) == "".join(w2lst)

# O(n) = nlog(n) or n^2

assert_true( is_anagram("python", "typhon") )
assert_true( is_anagram("dog", "god") )
assert_false( is_anagram("foo", "typhon") )
assert_false( is_anagram("abb", "baa") )

