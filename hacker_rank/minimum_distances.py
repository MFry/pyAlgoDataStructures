"""
    Difficulty: *
    Code:       *

    Ref: https://www.hackerrank.com/challenges/minimum-distances
"""
import unittest


def find_min_distance(arr):
    found = {}
    min_distance = float('inf')
    for i, val in enumerate(arr):
        if val in found:
            if min_distance > abs(found[val] - i):
                min_distance = abs(found[val] - i)
                found[val] = i
        else:
            found[val] = i
    min_distance = min_distance if min_distance != float('inf') else -1
    return min_distance


class MyTestCases(unittest.TestCase):
    def test_find_min_distance(self):
        arr = [7, 1, 3, 4, 1, 7]
        self.assertEqual(find_min_distance(arr), 3)


if __name__ == '__main__':
    n = int(input().strip())
    A = [int(A_temp) for A_temp in input().strip().split(' ')]
    print(find_min_distance(A))
