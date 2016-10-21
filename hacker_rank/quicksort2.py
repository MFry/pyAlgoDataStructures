"""
 Ref: https://www.hackerrank.com/challenges/quicksort2
"""
import unittest


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for ele in arr[1:]:
        if ele < pivot:
            left.append(ele)
        else:
            right.append(ele)
    if len(left) <= 1 and len(right) <= 1:
        temp = left + [pivot] + right
        print(' '.join([str(i) for i in temp]))
        return left + [pivot] + right
    temp = quicksort(left) + [pivot] + quicksort(right)
    print(' '.join([str(i) for i in temp]))
    return temp


class MyTestCases(unittest.TestCase):
    def test_quicksort(self):
        arr = [5, 8, 1, 3, 7, 9, 2]
        self.assertEqual(quicksort(arr), [1, 2, 3, 5, 7, 8, 9])
        arr = [9, 8, 6, 7, 3, 5, 4, 1, 2]
        self.assertEqual(quicksort(arr), [1, 2, 3, 4, 5, 6, 7, 8, 9])
