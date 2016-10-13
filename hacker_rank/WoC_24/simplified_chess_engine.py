"""

"""
import unittest


def get_moves(piece, r, c, board):
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
        return True

    def check_bounds(x, y):
        if x < 0 or y < 0:
            return False
        if x >= len(board) or y >= len(board):
            return False
        return True

    moves = []
    knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1)]
    bishop_moves = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    rook_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    p = piece['type']
    if p.lower() == 'n':
        for k_m in knight_moves:
            x, y = r + k_m[0], c + k_m[1]
            if check_bounds(x, y):
                moves.append((r + k_m[0], c + k_m[1]))
    elif p.lower() == 'q':
        for q_m in rook_moves+bishop_moves:
            x, y = r, c
            while True:
                x, y = x + q_m[0], y + q_m[1]
                if not check_bounds(x, y):
                    break
                moves.append((x, y))
    elif p.lower() == 'b':
        for b_m in bishop_moves:
            x, y = r, c
            while True:
                x, y = x + b_m[0], y + b_m[1]
                if not check_bounds(x, y):
                    break
                moves.append(x, y)

    elif p.lower() == 'r':
        for r_k in rook_moves:
            x, y = r, c
            while True:
                x, y = x + r_k[0], y + r_k[1]
                if not check_bounds(x, y):
                    break
                moves.append(x, y)
    return [i for i in moves if check_valid(*i)]


class MyTestCases(unittest.TestCase):
    def test_get_moves(self):
        board = [[{'type': 'q', 'color': 'b'}, '', '', ''],
                 ['', '', '', ''],
                 ['', {'type': 'n', 'color': 'w'}, '', ''],
                 ['', {'type': 'q', 'color': 'w'}, '', '']]
        self.assertEqual(board[2][1]['type'], 'n')
        self.assertEqual(get_moves(board[2][1], 2, 1, board), [(0, 2), (0, 0)])
        self.assertEqual(board[3][1]['type'], 'q')
        print(get_moves(board[3][1], 3, 1, board))
        # self.assertEqual(get_moves(board[3][1], 3, 1, board))
