"""
 Problem 12
 Data Structure, Skip List
"""
import unittest
from bisect import bisect_left


# Find in a list of n sorted integers a given int quickly


def binary_search(sorted_list, find_value, lower_bound=0, upper_bound=None):
    # Reference: http://stackoverflow.com/questions/212358/binary-search-bisection-in-python
    upper_bound = upper_bound or len(sorted_list)
    position = bisect_left(sorted_list, find_value, lower_bound, upper_bound)
    return position if position != upper_bound and sorted_list[position] == find_value else -1


class MyTestCases(unittest.TestCase):
    def test_binary_search(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEquals(binary_search(test_list, 6), 5)
        self.assertEqual(binary_search(test_list, 11), -1)
