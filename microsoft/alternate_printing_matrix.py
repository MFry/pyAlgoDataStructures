"""
    Suppose you have a matrix in the form of a 2 dimensional array. Write a method to read the rows of the matrix
     alternatively from right to left, left to right so on and return them as a 1 dimensional array.

        for eg:
        1 2 3
        4 5 6
        7 8 9

        e.x.  1 2 3 6 5 4 7 8 9
        Ref: https://www.careercup.com/question?id=5654187787419648
"""
import unittest


class AlternatingMatrix:
    def __init__(self, matrix):
        self._data = matrix

    def __str__(self):
        out = ''
        for i, row in enumerate(self._data):
            if i % 2 == 0:
                for ele in row:
                    out += str(ele) + ' '
            else:
                for j in range(len(row) - 1, -1, -1):
                    out += str(row[j]) + ' '
        return out


class MyTestCases(unittest.TestCase):
    def test_AlternatingMatrix(self):
        test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        alt_matrix = AlternatingMatrix(test_matrix)
        self.assertEqual(str(alt_matrix), '1 2 3 6 5 4 7 8 9 ')
