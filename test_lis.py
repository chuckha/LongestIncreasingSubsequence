import unittest

from lis import lis, lis2

class LISTestCase(unittest.TestCase):
    def setUp(self):
        list_1 = [6, 10, 11, 5, 8, 13, 9, 0, 3, 14, 7, 2, 4, 1, 12]
        list_1_lis =  [6, 10, 11, 13, 14]
        list_2 = [5, 12, 7, 14, 8, 0, 3, 9, 6, 13, 2, 11, 4, 10, 1]
        list_2_lis = [5, 7, 8, 9, 10]
        list_3 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        list_3_lis = [0, 2, 6, 9, 11, 15]
        self.lists = [list_1, list_2, list_3]
        self.list_lis = [list_1_lis, list_2_lis, list_3_lis]

    def test_lis(self):
        for l, longest_s in zip(self.lists, self.list_lis):
            self.assertEqual(longest_s, lis(l))

    def test_lis2(self):
        for l, longest_s in zip(self.lists, self.list_lis):
            self.assertEqual(len(longest_s), lis2(l))


if __name__ == '__main__':
    unittest.main()

