import unittest

from .sort_master import SortMaster


class TestSortMaster(unittest.TestCase):

    def test_create_random_sequence(self):
        s = SortMaster()
        seq = s.create_random_sequence()
        self.assertEqual(100, len(seq))

    def test_check_sorted(self):
        s = SortMaster()
        seq = s.create_random_sequence()
        self.assertEqual(False, s.check_sorted(seq)) # almost always
        self.assertEqual(True, s.check_sorted(sorted(seq) )) # almost always
