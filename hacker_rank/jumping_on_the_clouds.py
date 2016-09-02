"""
    Difficulty: *
    Code:       *
    ref: https://www.hackerrank.com/challenges/jumping-on-the-clouds
"""
import unittest


def cloud_jump(clouds):
    total = 0
    i = 0
    while i < len(clouds):
        jump = i + 2
        if jump >= len(clouds) - 1:
            total += 1
            break
        if not clouds[jump]:
            i = jump
        else:
            i = jump - 1
        total += 1
    return total


class MyTestCases(unittest.TestCase):
    def test_cloud_jump(self):
        clouds = [0, 0, 1, 0, 0, 1, 0]
        self.assertEqual(cloud_jump(clouds), 4)
