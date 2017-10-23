import unittest

from .mutable_string import MutableString

class TestMutableString(unittest.TestCase):

    def test_equality(self):
        a = MutableString("test 123 test")
        b = "test 123 test"
        self.assertEqual(a, b)

    def test_mutability(self):
        a = MutableString("test 123 test")
        a[0:4] = "helo"
        b = "helo 123 test"
        self.assertEqual(a, b)

    def test_len(self):
        a = MutableString("test 123 test")
        self.assertEqual(len(a), 13)
