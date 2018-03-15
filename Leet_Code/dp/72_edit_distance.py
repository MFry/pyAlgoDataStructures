import unittest


def min_distance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    memo = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
    for i in range(len(memo[0])):
        memo[0][i] = i
    for i in range(1, len(memo)):
        memo[i][0] = i
        for j in range(1, len(memo[0])):
            cost = 0 if word1[j - 1] == word2[i - 1] else 1
            memo[i][j] = min(memo[i - 1][j] + 1, memo[i][j - 1] + 1, memo[i - 1][j - 1] + cost)
    return memo[-1][-1]


class MyTestCases(unittest.TestCase):
    def test_min_distance(self):
        self.assertEqual(min_distance('', ''), 0)
        self.assertEqual(min_distance('ab', 'a'), 1)
        self.assertEqual(min_distance('dog', 'cat'), 3)
