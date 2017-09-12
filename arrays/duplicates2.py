import unittest


# O(n*k)
def contains_duplicates(lst, k):
    for i in range(len(lst)-1):
        for j in range(i+1, i+k):
            j = min(len(lst)-1, j)
            if lst[i] == lst[j]:
                return i, j
    return None, None


# O(n), O(n) memory for dict
def contains_duplicates_dict(lst, k):
    dct = dict()
    for i in range(len(lst)-1):
        if lst[i] not in dct:
            dct[lst[i]] = i
        elif i < dct[lst[i]] + k:
            return dct[lst[i]], i
    return None, None


class TestContainsDuplicates(unittest.TestCase):

    def test_contains_duplicates(self):
        a = list(range(100))
        i, j = contains_duplicates(a, 5)

        self.assertIsNone(i)
        self.assertIsNone(j)

        a[15] = 15
        a[20] = 15

        i, j = contains_duplicates(a, 6)
        self.assertEqual(i, 15)
        self.assertEqual(j, 20)

        i, j = contains_duplicates(a, 5)
        self.assertIsNone(i)
        self.assertIsNone(j)

    def test_contains_duplicates_dict(self):
        a = list(range(100))
        i, j = contains_duplicates_dict(a, 5)

        self.assertIsNone(i)
        self.assertIsNone(j)

        a[15] = 15
        a[20] = 15

        i, j = contains_duplicates_dict(a, 6)
        self.assertEqual(i, 15)
        self.assertEqual(j, 20)

        i, j = contains_duplicates_dict(a, 5)
        self.assertIsNone(i)
        self.assertIsNone(j)


if __name__=="__main__":
    unittest.main()
