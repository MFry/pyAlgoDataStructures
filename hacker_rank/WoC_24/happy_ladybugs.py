"""

"""
import unittest


def check_if_happy(board):
    prev = board[0]
    pairs = False
    for i in range(1, len(board)):
        if board[i] == '_':
            prev = '_'
            continue
        elif prev == '_':
            prev = board[i]
            pairs = False
            continue
        if board[i] == prev:
            pairs = True
        elif not pairs:
            return False
        else:
            pairs = False
            prev = board[i]
    if not pairs:
        return False
    return True


def happy_ladybugs(board):
    histogram = {}
    for cell in board:
        if cell in histogram:
            histogram[cell] += 1
        else:
            histogram[cell] = 1
    if '_' not in histogram:
        return check_if_happy(board)
    histogram.pop('_')
    for key in histogram:
        if histogram[key] == 1:
            return False
    return True


class MyTestCases(unittest.TestCase):
    def test_check_if_happy(self):
        b1 = 'RBY_YBR'
        self.assertFalse(check_if_happy(b1))
        b2 = 'RBYY_BR'
        self.assertFalse(check_if_happy(b2))
        b3 = 'R_YYBBR'
        self.assertFalse(check_if_happy(b3))
        b4 = 'RRRRRB_'
        self.assertFalse(check_if_happy(b4))
        b5 = '___RRR____BB_____CC_____'
        self.assertTrue(check_if_happy(b5))
        b6 = '_____________RRR_______________'
        self.assertTrue(check_if_happy(b6))
        b7 = 'B_B'
        self.assertFalse(check_if_happy(b7))

    def test_happy_ladybugs(self):
        b1 = 'RBY_YBR'
        self.assertTrue(happy_ladybugs(b1))
        b2 = 'X_Y__X'
        self.assertFalse(happy_ladybugs(b2))
        b3 = '__'
        self.assertTrue(happy_ladybugs(b3))
        b4 = '_'
        self.assertTrue(happy_ladybugs(b4))
        b5 = 'B_RRBR'
        self.assertTrue(happy_ladybugs(b5))
        b6 = b1 + b3 + b4 + b5
        self.assertTrue(happy_ladybugs(b6))


def main():
    q = int(input())
    for _ in range(q):
        _ = input()
        b = input().strip()
        if happy_ladybugs(b):
            print('YES')
        else:
            print('NO')
