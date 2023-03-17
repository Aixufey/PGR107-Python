import unittest
from task1 import k, h
from math import sqrt
help(unittest.TestCase.assertEqual)


class TestTaskOne(unittest.TestCase):
    def test_returnOfH(self):
        self.assertEqual(h(2), 9)
        self.assertEqual(h(0), 1)
        self.assertEqual(h(1), 4)

    def test_returnOfK(self):
        self.assertEqual(k(2), 6)
        self.assertEqual(k(-1), 0)
        self.assertEqual(k(0), 2)
        self.assertEqual(k(1), 4)
        self.assertEqual(k(9), 20)


if __name__ == '__main__':
    unittest.main()
