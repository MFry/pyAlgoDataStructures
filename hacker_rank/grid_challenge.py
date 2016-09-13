"""
Ref: https://www.hackerrank.com/challenges/grid-challenge
    ebacd
    fghij
    olmkn
    trpqs
    xywuv
"""
import unittest


def is_sortable(grid):
    sorted_grid = [[0] * len(grid)]
    for row in grid:
        characters = list(row)
        characters.sort(key=lambda x: ord(x))
        sorted_grid.append(characters)
    for j in range(len(grid[0])):
        for i in range(1, len(grid)):
            if grid[i][j] < grid[i - 1][j]:
                return False
    return True


class MyTestCases(unittest.TestCase):
    def test_is_sortable(self):
        grid = ['ebacd',
                'fghij',
                'olmkn',
                'trpqs',
                'xywuv']
        self.assertTrue(is_sortable(grid))
        grid = ['tjxxx',
                'xtxxj',
                'rzzzz',
                'zzrzz',
                'rzzzz']
        self.assertTrue(is_sortable(grid))


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        r = int(input())
        grid = []
        for __ in range(r):
            grid.append(input().strip())
        if is_sortable(grid):
            print('YES')
        else:
            print('NO')
