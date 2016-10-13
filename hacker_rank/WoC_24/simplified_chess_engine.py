"""

"""
import unittest


def get_moves(piece, c, r, board):
    def check_valid(x, y):
        """

        :param board: playing board
        :param c: pieces color
        :param x: coord
        :param y: coord
        :return: boolean
        """
        if board[x][y] and board[x][y]['color'] == piece['color']:
            return False
        if x < 0 or y < 0:
            return False
        elif x > len(board) or y > len(board):
            return False
        return True

    p = piece['type']
    if p.lower() == 'n':
        moves = [(r - 2, c - 1), (r - 2, c + 1), (r + 2, c - 1), (r + 2, c - 2)]
    elif p.lower() == 'q':
        pass
    elif p.lower() == 'b':
        moves = []
        for x in range(len(board)):
            for y in range(len(board)):
                moves.append((x, y))
                moves.append((y, x))
    elif p.lower() == 'r':
        moves = []
        for x in range(len(board)):
            moves.append((r, x))
        for y in range(len(board)):
            moves.append((y, c))
    return [i for i in moves if check_valid(*i)]


class MyTestCases(unittest.TestCase):
    def test_get_moves(self):
        board = [[{'type': 'q', 'color': 'b'}, '', '', ''],
                 ['', '', '', ''],
                 ['', {'type': 'n', 'color': 'w'}, '', ''],
                 ['', {'type': 'q', 'color': 'w'}, '', '']]
        print(get_moves(board[2][1], 2, 1, board))
