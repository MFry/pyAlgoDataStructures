import unittest


def spiral_print(matrix):
    """

    :param matrix:
    :type matrix: list of list
    :return:
    """

    out = ''

    i = 0
    j = 0
    # top side
    while j < len(matrix[i]):
        out += str(matrix[i][j]) + ' '
        j += 1
    i += 1
    j -= 1
    # right side
    while i < len(matrix):
        out += str(matrix[i][j]) + ' '
        i += 1
    i -= 1
    j -= 1
    # lower side
    while j >= 0:
        out += str(matrix[i][j]) + ' '
        j -= 1
    j += 1
    i -= 1
    # left side
    while i > 0:
        out += str(matrix[i][j]) + ' '
        i -= 1

    return out


class MyTestClass(unittest.TestCase):
    def test_spiral_print(self):
        self.assertEqual(spiral_print([[1, 2, 3],
                                      [4, 5, 6],
                                      [7, 8, 9]]), "1 2 3 6 9 8 7 4 ")
