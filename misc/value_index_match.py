"""
Given an array of sorted distinct integers named arr, write a function that returns an index i in arr
for which arr[i] = i or -1 if no such index exists.

Implement the most efficient solution possible, prove the correctness of your
solution and analyze its runtime complexity (in terms of n - the length of arr).

Reference: http://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/
"""
import unittest


def index_element_equality(arr):
    pass


class MyTestCase(unittest.TestCase):
    def test_index_element_equality(self):
        arr = [-8, 0, 2, 5]
        self.assertEqual(index_element_equality(arr), 2)
        arr = [-1, 0, 3, 6]
        self.assertEqual(index_element_equality(arr), -1)
