"""
Given an array of sorted distinct integers named arr, write a function that returns an index i in arr
for which arr[i] = i or -1 if no such index exists.

Implement the most efficient solution possible, prove the correctness of your
solution and analyze its runtime complexity (in terms of n - the length of arr).

Reference: http://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/
"""
import unittest


def index_element_equality(arr):
    lower_bound = 0
    upper_bound = len(arr) - 1
    while lower_bound <= upper_bound:
        mid_point = lower_bound + (upper_bound - lower_bound) // 2
        if mid_point == arr[mid_point]:
            return mid_point
        elif mid_point > arr[mid_point]:
            lower_bound = mid_point + 1
        elif mid_point < arr[mid_point]:
            upper_bound = mid_point - 1
    return -1


class MyTestCase(unittest.TestCase):
    def test_index_element_equality(self):
        arr = [-8, 0, 2, 5]
        self.assertEqual(index_element_equality(arr), 2)
        arr = [-1, 0, 3, 6]
        self.assertEqual(index_element_equality(arr), -1)
        arr = [-1, 1]
        self.assertEqual(index_element_equality(arr), 1)
