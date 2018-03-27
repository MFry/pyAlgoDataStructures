import unittest
"""
 Problem 15
"""
# TODO: Look at solution that takes O(lg n) time


def find_nth_fib(n):
    if n < 0:
        raise IndexError("Index {} is negative.".format(n))
    if n == 0 or n == 1:
        return n
    nth_fib_number = 0
    prev_fib = 0
    current_fib = 1
    while n > 1:
        nth_fib_number = current_fib + prev_fib
        prev_fib = current_fib
        current_fib = nth_fib_number
        n -= 1
    return nth_fib_number


class TestMyCases(unittest.TestCase):
    def test_find_nth_fib(self):
        self.assertEqual(find_nth_fib(0), 0)
        self.assertEqual(find_nth_fib(1), 1)
        self.assertEqual(find_nth_fib(3), 2)
        self.assertEqual(find_nth_fib(4), 3)
