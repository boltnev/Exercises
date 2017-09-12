import unittest


def rotate_list(lst, k):
    for _ in range(k):
        lst.insert(0, lst.pop())
    return lst


def swap(seq, i, j):
    temp = seq[j]
    seq[j] = seq[i]
    seq[i] = temp

# O(n*k)
def rotate_array_naive(arr, k):
    for _ in range(k):
        for i in range(len(arr)):
            swap(arr, i, 0)

    return arr


# O(n)
def rotate_array(arr, k):
    k = k % len(arr)
    for i in range(len(arr) - len(arr) % k):
        j = i % k
        swap(arr, j, (i+k) % len(arr))
    return arr


class TestRotateArrayList(unittest.TestCase):

    def test_rotate_list(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 3
        b = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

        self.assertEqual(b, rotate_list(a, k))

    def test_rotate_array_naive(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 3
        b = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

        self.assertEqual(b, rotate_array_naive(a, k))

    def test_rotate_array(self):

        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 4
        b = [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]

        self.assertEqual(b, rotate_array(a, k))

        a = list(range(100))
        k = 8
        b = rotate_array_naive(list(range(100)), k)

        self.assertEqual(b, rotate_array(a, k))

        a = list(range(100))
        k = 11
        b = rotate_array_naive(list(range(100)), k)

        self.assertEqual(b, rotate_array(a, k))

        a = list(range(100))
        k = 105
        b = rotate_array_naive(list(range(100)), k)

        self.assertEqual(b, rotate_array(a, k))

if __name__=="__main__":
    unittest.main()
