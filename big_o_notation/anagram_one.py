from nose.tools import assert_true, assert_false

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    w1lst = list(word1)
    w2lst = list(word2)

    for i in range(0, len(word1)):
        for j in range(0, len(word1)):
            if w1lst[i] == w2lst[j]:
                w1lst[i] = '#'
                w2lst[j] = '#'
                break

    #print(w1lst)
    #print(w2lst)
    return ''.join(w1lst) == '#' * len(word2)

# O(n) = n(2n) + n -> O(n^2)

assert_true( is_anagram("python", "typhon") )
assert_true( is_anagram("dog", "god") )
assert_false( is_anagram("cat", "foo") )
assert_false( is_anagram("dog", "bird") )
assert_false( is_anagram("abb", "aab") )
