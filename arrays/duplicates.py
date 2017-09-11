import unittest

def contains_duplicates(lst):
    return len(set(lst)) < len(lst)


def contains_duplicates_in_place(lst):
    for i, item in enumerate(lst):
        if i == len(lst):
            return False
        if item in lst[i+1:]:
            return True


class TestContainsDuplicates(unittest.TestCase):

    def test_contains_duplicates(self):
        a = [1, 2, 3, 4, 5, 6]
        self.assertFalse(contains_duplicates(a))

        a = [1, 2, 3, 4, 5, 6, 6, 4, 3]
        self.assertTrue(contains_duplicates(a))

        a = 'abcdec'
        self.assertTrue(contains_duplicates(a))

    def test_contains_duplicates_in_place(self):
        a = [1, 2, 3, 4, 5, 6]
        self.assertFalse(contains_duplicates_in_place(a))

        a = [1, 2, 3, 4, 5, 6, 6, 4, 3]
        self.assertTrue(contains_duplicates_in_place(a))

        a = 'abcdec'
        self.assertTrue(contains_duplicates_in_place(a))


if __name__=="__main__":
    unittest.main()
