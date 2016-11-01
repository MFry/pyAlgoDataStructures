"""
    Difficulty: ***
    Code:       **
    Required Knowledge: Dynamic Programming
    Ref: https://www.hackerrank.com/challenges/maxsubarray
"""
import unittest


def max_subarray(arr):
    largest_val = float('-inf')
    non_contiguous = 0
    contiguous = 0
    cur = 0
    for num in arr:
        if num > largest_val:
            largest_val = num
        if num > 0:
            non_contiguous += num
        if num + cur < 0:
            cur = 0
            continue
        cur += num
        if cur > contiguous:
            contiguous = cur
    if largest_val < 0:
        return largest_val, largest_val
    return contiguous, non_contiguous


class MyTestCases(unittest.TestCase):
    def test_max_subarray(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(max_subarray(arr), (10, 10))
        arr = [2, -1, 2, 3, 4, -5]
        self.assertEqual(max_subarray(arr), (10, 11))


"""
import sys
sys.
"""
