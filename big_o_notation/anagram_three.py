from nose.tools import assert_true, assert_false

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    w1lst = [0] * 26
    w2lst = [0] * 26

    for ch in word1:
        idx = ord(ch) - ord('a')
        w1lst[idx] = w1lst[idx] + 1

    for ch in word2:
        idx = ord(ch) - ord('a')
        w2lst[idx] = w2lst[idx] + 1

    return w1lst == w2lst


# O(n) = 2n + 26 -> n

assert_false( is_anagram('foo', 'py') )
assert_false( is_anagram('foo', 'bar') )
assert_true( is_anagram('python', 'typhon') )
assert_true( is_anagram('abcd', 'dcab') )
assert_false( is_anagram('abbcd', 'baacd') )
