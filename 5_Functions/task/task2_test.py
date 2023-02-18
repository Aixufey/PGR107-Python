import unittest
from task2 import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_5(self):
        self.assertEqual(factorial(5), 120)

