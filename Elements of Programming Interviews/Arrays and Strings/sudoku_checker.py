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
            x, y = key
            x, y = SudokuBoard._convert_index(x, y)
            self._used_numbers[value] = value
            self._block[x][y] = value

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

    def __str__(self):
        out = ''
        for row in self._board:
            out += '|'
            for i in len(row):
                for j, _ in enumerate(row):
                    out += row[j][i]

    def __getitem__(self, item):
        x, y = item
        row, column = self._convert_index(x, y)
        return self._board[row][column]

    def __setitem__(self, key, value):
        x, y = key
        row, column = self._convert_index(x, y)
        self._board[row][column][x % 3][x % 3] = value


class MyTestCase(unittest.TestCase):
    def test_sudoku_access(self):
        t = SudokuBoard()
        t[0, 0] = 1
        t[8, 8] = 8
        print(t)


if __name__ == '__main__':
    unittest.main()
