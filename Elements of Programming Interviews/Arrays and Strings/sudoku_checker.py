import unittest


class SudokuBoard:
    class SudokuSubBoard:

        def __init__(self, *args):
            self._used_numbers = [0] * 9
            self._block = [[0, 0, 0] for _ in range(3)]

        def _is_valid(self):
            for check in self._used_numbers:
                if check > 1:
                    return False

        def check(self):
            return self._is_valid()

        def __setitem__(self, key, value):
            if 9 < value < 0:
                raise ValueError('Number ' + str(value) + ' is out of bounds')
            self._used_numbers[value] = value
            self._block[key] = value

        def __getitem__(self, item):
            return self._block[item]

    def __init__(self):
        self._board = [[SudokuBoard.SudokuSubBoard(),
                        SudokuBoard.SudokuSubBoard(),
                        SudokuBoard.SudokuSubBoard()] for _ in range(3)]

    @staticmethod
    def _convert_index(row, column):
        if 9 < row < 0 or 9 < column < 0:
            raise IndexError('Row: ' + str(row) + ' Column: ' + str(column) + ' out of bound.')
        row //= 3
        column //= 3
        return row, column

    def __getitem__(self, item):
        x, y = item
        row, column = self._convert_index(x, y)
        return self._board[row][column]

    def __setitem__(self, key, value):
        x, y = key
        row, column = self._convert_index(x, y)
        index = row % 3 + column % 3
        self._board[row][column][index] = value


class MyTestCase(unittest.TestCase):
    def test_sudoku_access(self):
        t = SudokuBoard()
        t[0, 0] = 1
        t[8, 8] = 8
        print(t)


if __name__ == '__main__':
    unittest.main()
