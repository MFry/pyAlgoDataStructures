"""
 ref: https://www.hackerrank.com/contests/w24/challenges/simplified-chess-engine
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

    def gen_moves(moves):
        valid_moves = []
        for move in moves:
            x, y = r, c
            while True:
                x, y = x + move[0], y + move[1]
                if not check_bounds(x, y) or check_valid(x, y):
                    break
                valid_moves.append((x, y))
                if board[x][y] != piece['color']:
                    break
        return valid_moves

    moved = []
    knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1)]
    bishop_moves = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    rook_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    p = piece['type']
    # knight
    if p.lower() == 'n':
        for k_m in knight_moves:
            x, y = r + k_m[0], c + k_m[1]
            if check_bounds(x, y):
                moved.append((r + k_m[0], c + k_m[1]))
    # Bishop
    elif p.lower() == 'b':
        moved = gen_moves(bishop_moves)

    # Rook
    elif p.lower() == 'r':
        moved = gen_moves(rook_moves)

    # Queen
    elif p.lower() == 'q':
        moved = gen_moves(bishop_moves+rook_moves)
    return moved


class MyTestCases(unittest.TestCase):
    def test_get_moves(self):
        board = [[{'type': 'q', 'color': 'b'}, '', ''],
                 ['', '', '', ''],
                 ['', {'type': 'n', 'color': 'w'}, '', ''],
                 ['', {'type': 'q', 'color': 'w'}, '', '']]
        #check we selected a knight
        self.assertEqual(board[2][1]['type'], 'n')
        # knight moves
        self.assertEqual(get_moves(board[2][1], 2, 1, board), [(0, 2), (0, 0)])

        self.assertEqual(board[3][1]['type'], 'q')
        print(get_moves(board[3][1], 3, 1, board))
        # self.assertEqual(get_moves(board[3][1], 3, 1, board))
