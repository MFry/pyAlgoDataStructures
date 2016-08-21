"""

"""
import unittest


def flood_fill(island_map, i, j):

    def check_range(loc):
        if loc[0] < 0 or loc[0] >= len(island_map):
            return False
        if loc[1] < 0 or loc[1] >= len(island_map[loc[0]]):
            return False
        return True

    queue = [(i, j)]
    while queue:
        # pick top from queue
        i, j = queue.pop(0)
        # switch current coord to 0
        island_map[i][j] = 0
        # top
        # left
        # right
        # bottom
        # loc : (1,1) (0,0)
        for loc in [(i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j)]:
            if check_range(loc) and island_map[loc[0]][loc[1]] == 1:
                queue.append(loc)
    return None


def island_count(island_map):
    islands_found = 0
    for i in range(len(island_map)):
        for j in range((len(island_map[i]))):
            if island_map[i][j] == 1:
                islands_found += 1
                flood_fill(island_map, i, j)
    return islands_found


class MyTestCases(unittest.TestCase):
    def test_island_found(self):
        island_map = [[0, 1, 0, 1, 0],
                     [0, 0, 1, 1, 1],
                     [1, 0, 0, 1, 0],
                     [0, 1, 1, 0, 0],
                     [1, 0, 1, 0, 1]]
        self.assertEqual(island_count(island_map), 6)
