"""
Given a floor of dimensions 2 x W and tiles of dimensions 2 x 1,
write code to find the number of ways the floor can be tiled.
A tile can either be placed horizontally i.e as a 1 x 2 tile or vertically i.e as 2 x 1 tile.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is W.

Output:

Print number of ways the floor can be tiled in a separate line.

Constraints:

1 ≤ T ≤ 50
1 ≤ W ≤ 70

Example:

Input
2
5
3

Output
8
3
"""
import unittest


def fib_tiles(W):
    combinations = 0
    prev = 0
    current = 1
    for i in range(W):
        combinations = prev + current
        prev = current
        current = combinations
    return combinations


class MyTestCases(unittest.TestCase):
    def test_fib_tiles(self):
        self.assertEqual(fib_tiles(1), 1)
        self.assertEqual(fib_tiles(2), 2)
        self.assertEqual(fib_tiles(3), 3)
        self.assertEqual(fib_tiles(5), 8)
