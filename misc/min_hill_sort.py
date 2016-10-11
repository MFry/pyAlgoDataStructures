"""

"""
import unittest


def check_valid(arr, x):
    temp_arr = arr[:]
    temp_arr[0] = arr[0] - x
    for i in range(1, len(arr)):
        if temp_arr[i-1] < x + temp_arr[i]:
            temp_arr[i] = max(temp_arr[i-1]+1, temp_arr[i]-x)
        else:
            return False
    return True


def min_to_sort(arr):
    low = 1
    high = 2**31 - 1
    result = -1
    while low < high:
        mid = (high + low)//2
        if check_valid(arr, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result


class MyTestResults(unittest.TestCase):
    def test_check_valid(self):
        arr = [5, 4, 3, 2, 8]
        self.assertTrue(check_valid(arr, 500))
        self.assertTrue(check_valid(arr, 5))
        self.assertTrue(check_valid(arr, 4))
        self.assertTrue(check_valid(arr, 3))
        self.assertFalse(check_valid(arr, 2))
        self.assertFalse(check_valid(arr, 1))
        self.assertFalse(check_valid(arr, 1))
        arr = [52, 71, 36, 92, 48]
        self.assertTrue(check_valid(arr, 23))

    def test_min_to_sort(self):
        arr = [5, 4, 3, 2, 8]
        self.assertEqual(min_to_sort(arr), 3)
        arr = [52, 71, 36, 92, 48]
        self.assertEqual((check_valid(arr, 23)))
