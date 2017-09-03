import unittest

from tools.sort_master import SortMaster


def swap(seq, i, j):
    temp = seq[j]
    seq[j] = seq[i]
    seq[i] = temp


def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    pivot = seq[-1]
    leftpart = 0
    for i in range(len(seq)-1):
        if seq[i] <= pivot:
            swap(seq, i, leftpart)
            leftpart+=1
        
    swap(seq, -1, leftpart)
    print("{}..{} {}..{}".format(0, leftpart, leftpart+1, len(seq)))
    return quick_sort(seq[0:leftpart]) + [pivot] + quick_sort(seq[leftpart+1:])


class QuickSortTets(unittest.TestCase):

    def test_sorted(self):
        s = SortMaster()
        seq = s.create_random_sequence()
        self.assertFalse(s.check_sorted(seq))
        seq = quick_sort(seq)
        self.assertTrue(s.check_sorted(seq))
        self.assertEqual(len(seq), 100)