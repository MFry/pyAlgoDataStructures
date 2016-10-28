"""

Problem Reference: https://www.hackerrank.com/contests/w24/challenges/xor-matrix


Difficulty: ****
Required Knowledge: Combinatorics, Pascal's triangle
"""
from pprint import pprint
from operator import xor
import unittest

test = [6, 7, 1, 3]


def get_xor_matrix(row, total_columns):
    matrix = [row]
    for i in range(total_columns):
        temp = []
        for j in range(len(row)):
            left = j
            right = j + 1
            if right == len(row):
                right = 0
            test = matrix[-1]
            temp.append(xor(matrix[-1][left], matrix[-1][right]))
        matrix.append(temp)
    return matrix


def fast_xor_row(row, depth):
    partial_matrix = [row]
    base2 = 1
    c = depth
    while c > 0:
        if c % 2 == 1:
            t = []
            for i in range(len(row)):
                t.append(xor(partial_matrix[-1][i], partial_matrix[-1][(i + base2) % len(row)]))
            partial_matrix.append(t)
        base2 *= 2
        c //= 2

    return partial_matrix[-1]


class MyTestCases(unittest.TestCase):
    def test_fast_xor_row(self):
        #pprint(get_xor_matrix(test, 5))
        test = get_xor_matrix([6,7,1,3], 2)
        self.assertEqual(fast_xor_row([6,7,1,3], 10), test[-1])
