"""
    Difficulty: **
    Code: *
I have a list where every number in the range 1...n appears once except for one number which appears twice.
Write a function for finding the number that appears twice.


Hints: Look Triangular series
"""
import unittest


def find_duplicate(number_list):
    n = (len(number_list) - 1)
    sum_to_n = ((n ** 2) * n) / 2
    number_list_sum = 0
    for num in number_list:
        number_list_sum += num
    return number_list_sum - sum_to_n


class MyTestCases(unittest.TestCase):
    def test_find_duplicate(self):
        pass
