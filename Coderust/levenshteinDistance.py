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
    memo = [[0 for i in range(len(s1))] for j in range(len(s2))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[:i] == s2[:j]:
                memo[i][j] = 0
            else:
                memo[i][j] = min(memo[i-1][j]+1, memo[i][j-1]+1, memo[i-1]memo[j-1])



class TestLevenshteinDistance(unittest.TestCase):

    def test_bruteforce(self):
        self.assertEqual(min_distance('ant', 'ant'), 0)
        self.assertEqual(min_distance('test', 'text'), 1)
        self.assertEqual(min_distance('ant', 'aunt'), 1)
        self.assertEqual(min_distance('min', 'max'), 2)
