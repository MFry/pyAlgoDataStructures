"""
 ref: https://www.hackerrank.com/contests/w25/challenges/baby-step-giant-step
"""
import unittest
import math


def min_steps(a, b, end):
    if end == 0:
        return 0
    elif a == end:
        return 1
    elif end < b:
        return 2
    else:
        return math.ceil(end / b)


class MyTestCases(unittest.TestCase):
    def test_min_steps(self):
        self.assertEqual(min_steps(1, 2, 1), 1)
        self.assertEqual(min_steps(2, 11, 3), 2)
        self.assertEqual(min_steps(2, 4, 15), 4)


def main():
    q = int(input())
    for _ in range(q):
        a, b, end = [int(i) for i in input().split()]
        print(min_steps(a, b, end))


if __name__ == '__main__':
    main()
