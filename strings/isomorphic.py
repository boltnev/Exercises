import unittest


# O(N)
def is_isomorphic(a, b):
    if len(a) == len(b):
        def get_unified_mapping(a):
            mapping = {}
            unified_arr = []
            counter = 0
            for l in a:
                if l not in mapping:
                    mapping[l] = counter
                    counter += 1
                unified_arr.append(mapping[l])
            return unified_arr
        return get_unified_mapping(a) == get_unified_mapping(b)

    return False


class IsIsomorphicTest(unittest.TestCase):

    def test_is_isomorphic(self):
        a = "abba"
        b = "geeg"
        c = "abeg"
        d = "abbba"
        f = "isssi"

        self.assertTrue(is_isomorphic(a, b))
        self.assertFalse(is_isomorphic(a, c))
        self.assertFalse(is_isomorphic(a, d))
        self.assertTrue(is_isomorphic(d, f))

if __name__=="__main__":
    unittest.main()
