import unittest


def spiral_print(matrix):
    """

    :param matrix:
    :type matrix: list of list
    :return:
    """

    out = ''

    offset_i = 0
    offset_j = 0
    while offset_i <  len(matrix):
        i = offset_i
        j = offset_j
        # top side
        while j < len(matrix[i]) - offset_j:
            out += str(matrix[i][j]) + ' '
            j += 1
        i += 1
        j -= 1
        # right side
        while i < len(matrix) - offset_j:
            out += str(matrix[i][j]) + ' '
            i += 1
        i -= 1
        j -= 1
        # lower side
        while j >= offset_j:
            out += str(matrix[i][j]) + ' '
            j -= 1
        j += 1
        i -= 1
        # left side
        while i > offset_i:
            out += str(matrix[i][j]) + ' '
            i -= 1
        offset_i += 1
        offset_j += 1

    return out


class MyTestClass(unittest.TestCase):
    def test_spiral_print(self):
        self.assertEqual(spiral_print([[1, 2, 3],
                                      [4, 5, 6],
                                      [7, 8, 9]]), "1 2 3 6 9 8 7 4 5 ")
        self.assertEqual(spiral_print([[1, 2, 3, 4, 5],
                                       [6, 7, 8, 9, 10],
                                       [11, 12, 13, 14, 15],
                                       [16, 17, 18, 19, 20],
                                       [21, 22, 23, 24, 25]]),
                         "1 2 3 4 5 10 15 20 25 24 23 22 21 16 11 6 7 8 9 14 19 18 17 12 13 ")
