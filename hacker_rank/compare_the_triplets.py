"""
    Difficulty: *
    Code:       *

    Ref: https://www.hackerrank.com/challenges/compare-the-triplets
"""
import unittest


def compare_triplets(a, b):
    left_out = 0
    right_out = 0
    for i, j in zip(a, b):
        if i > j:
            left_out += 1
        elif i < j:
            right_out += 1
    return left_out, right_out


class MyTestCase(unittest.TestCase):
    def test_compare_triplets(self):
        a = [5, 6, 7]
        b = (3, 6, 10)
        self.assertEqual(compare_triplets(a, b), (1, 1))
