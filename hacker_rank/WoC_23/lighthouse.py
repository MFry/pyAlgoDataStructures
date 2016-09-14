"""
    ref: https://www.hackerrank.com/contests/w23/challenges/lighthouse
    Python
    ref: https://pymotw.com/3/collections/deque.html
"""
import unittest
from collections import deque


def within_bounds(coords, **kwargs):
    (x, y) = coords
    if kwargs['top'] <= x < kwargs['bot'] and kwargs['left'] <= y < kwargs['right']:
        return True
    return False


def check_voxel_circle(grid, x, y):
    bounds = {
        'top': 0,
        'left': 0,
        'bot': len(grid),
        'right': len(grid)
    }
    q = deque()
    q.append((x, y))
    visited = set()
    visited.add((x, y))
    radius_size = 0
    temp = deque()
    while True:
        if not q and not temp:
            break
        elif not q:
            radius_size += 1
            q, temp = temp, deque()
        (x, y) = q.popleft()
        top = (x - 1, y)
        left = (x, y - 1)
        bot = (x + 1, y)
        right = (x, y + 1)
        for coords in [top, left, bot, right]:
            if not within_bounds(coords, **bounds) or grid[coords[0]][coords[1]] == '*':
                return radius_size
            elif coords not in visited:
                temp.append(coords)
                visited.add(coords)
    return radius_size


class MyTestCases(unittest.TestCase):
    def test_within_bounds(self):
        bounds = {
            'top': 0,
            'left': 0,
            'bot': 11,
            'right': 11
        }
        for i in range(11):
            for j in range(11):
                self.assertTrue(within_bounds((i, j), **bounds))
        self.assertFalse(within_bounds((-1, 0), **bounds))
        self.assertFalse(within_bounds((0, -1), **bounds))
        self.assertFalse(within_bounds((11, 5), **bounds))
        self.assertFalse(within_bounds((8, 11), **bounds))

    def test_check_voxel_circle(self):
        grid = ['.....',
                '.....',
                '.....',
                '.....',
                '.....']
        self.assertEqual(check_voxel_circle(grid, 2, 2), 2)
        grid = ['.....',
                '.*...',
                '.....',
                '.....',
                '.....']
        self.assertEqual(check_voxel_circle(grid, 2, 2), 1)
        grid = ['.....',
                '.....',
                '.*...',
                '.....',
                '.....']
        self.assertEqual(check_voxel_circle(grid, 2, 2), 0)
        grid = ['.*.*.',
                '*...*',
                '.....',
                '*...*',
                '.*.*.']
        self.assertEqual(check_voxel_circle(grid, 2, 2), 2)
        grid = ['*********',
                '****.****',
                '**.....**',
                '**.....**',
                '*.......*',
                '**.....**',
                '**.....**',
                '****.****',
                '*********']
        self.assertEqual(check_voxel_circle(grid, 4, 4), 3)
        grid = ['*****.*****',
                '**.......**',
                '*.........*',
                '*.........*',
                '*.........*',
                '...........',
                '*.........*',
                '*.........*',
                '*.........*',
                '**.......**',
                '*****.*****']
        self.assertEqual(check_voxel_circle(grid, 5, 5), 5)
        radius = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == '.':
                    r = check_voxel_circle(grid, i, j)
                    if radius < r:
                        radius = r
        self.assertEqual(radius, 5)
        grid = ['.*.',
                '*.*',
                '.*.']
        radius = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == '.':
                    r = check_voxel_circle(grid, i, j)
                    if radius < r:
                        radius = r
        self.assertEqual(radius, 0)
        grid = ['*****.*****',
                '**.......**',
                '*.........*',
                '*...*.....*',
                '*.........*',
                '...........',
                '*.........*',
                '*.........*',
                '*.........*',
                '**.......**',
                '*****.*****']
        self.assertEqual(check_voxel_circle(grid, 5, 5), 2)
        grid = ['...........',
                '...........',
                '...........',
                '...........',
                '...........',
                '...........',
                '...........',
                '...........',
                '...........',
                '...........',
                '...........']
        self.assertEqual(check_voxel_circle(grid, 5, 5), 5)
        grid = ['*****.*****',
                '**.......**',
                '*.........*',
                '*.........*',
                '*.........*',
                '..........*',
                '*.........*',
                '*.........*',
                '*.........*',
                '**.......**',
                '*****.*****']
        self.assertEqual(check_voxel_circle(grid, 5, 5), 4)
        grid = ['.....',
                '.....',
                '.....',
                '...*.',
                '.....']
        self.assertEqual(check_voxel_circle(grid, 2, 2), 1)
        grid = ['.....',
                '.....',
                '.....',
                '.*...',
                '.....']
        self.assertEqual(check_voxel_circle(grid, 2, 2), 1)
        grid = ['.....',
                '...*.',
                '.....',
                '.....',
                '.....']
        self.assertEqual(check_voxel_circle(grid, 2, 2), 1)
        grid = ['......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................']
        radius = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == '.':
                    r = check_voxel_circle(grid, i, j)
                    if radius < r:
                        radius = r
        self.assertEqual(radius, 10)
        grid = ['......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',  # mid
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '**********************',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................',
                '......................']
        radius = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == '.':
                    r = check_voxel_circle(grid, i, j)
                    if radius < r:
                        radius = r
        self.assertEqual(radius, 5)
        grid = ['..',
                '..']
        self.assertEqual(check_voxel_circle(grid, 2, 2), 0)
        grid = ['....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................',
                '....................']
        self.assertEqual(check_voxel_circle(grid, 10, 10), 9)
        self.assertEqual(check_voxel_circle(grid, 2, 2), 2)
        grid = ['.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........',
                '.........*..........']
        radius = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == '.':
                    r = check_voxel_circle(grid, i, j)
                    if radius < r:
                        radius = r
        self.assertEqual(radius, 4)


if __name__ == '__main__':
    size = int(input())
    grid = []
    for row in range(size):
        grid.append(input().strip())
    largest_radius = -1
    for i in range(size):
        for j in range(size):
            if grid[i][j] == '.':
                r = check_voxel_circle(grid, i, j)
                if r > largest_radius:
                    largest_radius = r
    print(largest_radius)
