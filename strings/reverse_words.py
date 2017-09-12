import unittest

from tools.mutable_string import MutableString

# https://www.programcreek.com/2014/05/leetcode-reverse-words-in-a-string-ii-java/

def reverse_words(string):
    string = MutableString(string)
    word_begin = None

    for i in range(len(string)):
        if string[i] == ' ' and word_begin is not None:
            string[word_begin:i] = reversed(string[word_begin:i])
            word_begin = None
        else:
            if word_begin is None:
                word_begin = i

    if word_begin is not None:
        string[word_begin:len(string)] = reversed(string[word_begin:len(string)])
    print(string)

    return reversed(string)


class TestReverseWords(unittest.TestCase):

    def test_reverse_words(self):
        a = "big brown fox jumps"
        b = "jumps fox brown big"

        self.assertEqual(a, reverse_words(b))
