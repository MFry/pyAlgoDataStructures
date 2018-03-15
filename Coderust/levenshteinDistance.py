import unittest


def min_distance(s1, s2, cost=0):
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    if s1[-1] != s2[-1]:
        cost = 1
    d1 = min_distance(s1[:-1], s2)+1
    d2 = min_distance(s1, s2[:-1])+1
    d3 = min_distance(s1[:-1], s2[:-1])+cost
    return min(d1, d2, d3)


def levenshtein_distance_2d(s1, s2):
    memo = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
    for i in range(len(s1)):
        memo[0][i] = i
    for i in range(1, len(s1)):
        memo[i][0] = i
        for j in range(1, len(s2)):
            cost = 1 if s1[j-1] != s2[i-1] else 0
            memo[i][j] = min(memo[i-1][j]+1, memo[i][j-1]+1, memo[i-1][j-1]+cost)
    return memo[-1][-1]


class TestLevenshteinDistance(unittest.TestCase):

    def test_bruteforce(self):
        self.assertEqual(min_distance('ant', 'ant'), 0)
        self.assertEqual(min_distance('test', 'text'), 1)
        self.assertEqual(min_distance('ant', 'aunt'), 1)
        self.assertEqual(min_distance('min', 'max'), 2)
        self.assertEqual(min_distance('cat', 'dog'), 3)

    def test_dp_2d(self):
        self.assertEqual(levenshtein_distance_2d('ant', 'ant'), 0)
        self.assertEqual(levenshtein_distance_2d('test', 'text'), 1)
        self.assertEqual(levenshtein_distance_2d('ant', 'aunt'), 1)
        self.assertEqual(levenshtein_distance_2d('min', 'max'), 2)
        self.assertEqual(levenshtein_distance_2d('cat', 'dog'), 3)
