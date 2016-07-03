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
            for i in range(len(row)):
                out += '|'
                for j, _ in enumerate(row):
                    out += str(self._board[j][i])
                out += '|\n'
        return out

    def __getitem__(self, item):
        x, y = item
        row, column = self._convert_index(x, y)
        return self._board[row][column]

    def __setitem__(self, key, value):
        x, y = key
        row, column = self._convert_index(x, y)
        self._board[row][column][x % 3][x % 3] = value


def check_sudoku(board):
    """
        Given a 9 x 9 board check whether the sudoku is valid or partially valid
    :param board:
     :type board: list of list
    :return:
    :rtype: bool
    """
    # XXX XXX XXX
    # XXX XXX XXX
    # XXX XXX XXX

    # XXX XXX XXX
    # XXX XXX XXX
    # XXX XXX XXX

    # XXX XXX XXX
    # XXX XXX XXX
    # XXX XXX XXX

    # check the rows
    for i, row in enumerate(board):
        valid_row = [False] * (len(row) + 1)
        for j, val in enumerate(row):
            if valid_row[val]:
                return False
            if val != 0:
                valid_row[val] = True

    # check the columns
    for i, _ in enumerate(board[0]):
        valid_row = [False] * (len(board) + 1)
        for j, _ in enumerate(board):
            if valid_row[board[j][i]]:
                return False
            if val != 0:
                valid_row[board[j][i]] = True

    # check the blocks
    block_row = 0
    block_column= 0
    i = 0
    while i < len(board):
        j = 0
        while j < len(board):
            block_check = [False] * (len(board) + 1)
            while block_row < 3:
                block_column = 0
                while block_column < 3:
                    if block_check[board[i+block_row][j+block_column]]:
                        return False
                    if board[i+block_row][j+block_column]:
                        block_check[board[i+block_row][j+block_column]] = True
                    block_column += 1
                block_row += 1
            block_row = 0
            j += 3
        i += 3

    return True


class MyTestCase(unittest.TestCase):
    def test_sudoku_access(self):
        t = SudokuBoard()
        t[0, 0] = 1
        t[8, 8] = 8
        # print(t)

    def test_check_sudoku(self):
        test_board = [[1, 2, 3, 4, 0, 6, 7, 0, 9],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertTrue(check_sudoku(test_board))
        test_board = [[1, 2, 3, 4, 0, 6, 7, 0, 9],
                      [2, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertFalse(check_sudoku(test_board))
        test_board = [[1, 2, 3, 0, 0, 6, 7, 0, 9],
                      [5, 6, 7, 0, 0, 0, 0, 0, 0],
                      [4, 0, 9, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 2, 0, 0, 0, 0, 0],
                      [0, 0, 0, 2, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertFalse(check_sudoku(test_board))


if __name__ == '__main__':
    unittest.main()
