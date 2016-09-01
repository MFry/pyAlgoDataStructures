"""
    Difficulty: *
    Code:       *
    Ref: https://www.hackerrank.com/challenges/divisible-sum-pairs
"""
import unittest


def divisible_sum_pairs(numbers, k):
    divisible = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) % k == 0:
                divisible += 1
    return divisible


class MyTestCases(unittest.TestCase):
    def test_divisible_sum_pairs(self):
        numbers = [1, 3, 2, 6, 1, 2]
        self.assertEqual(divisible_sum_pairs(numbers, 3), 5)
