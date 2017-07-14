"""
 Type: DP, string
"""
import unittest


# Base case where at least one string is empty
def deletion_distance_base(str1, str2):
    deletions = 0
    if len(str1) == 0 or len(str2) == 0:
        return max(len(str1), len(str2)) + deletions


def deletion_distance_recursive(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return max(len(str1), len(str2))
    # To help with readability
    d = deletion_distance_recursive
    if str1[-1] == str2[-1]:
        return 0 + d(str1[:-1], str2[:-1])
    return 1 + min(d(str1[:-1], str2), d(str1, str2[:-1]))


def deletion_distance_2d_dp(str1, str2):
    optimal = [[0 for x in range(len(str2)+1)] for x in range(len(str1)+1)]
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i == 0:
                optimal[i][j] = j
            elif j == 0:
                optimal[i][j] = i
            elif str1[i-1] == str2[j-1]:
                optimal[i][j] = optimal[i-1][j-1]
            else:
                optimal[i][j] = 1 + min(optimal[i-1][j], optimal[i][j-1])
    return optimal[-1][-1]


def deletion_distance_1d_dp(str1, str2):
    if len(str2) > len(str1):
        str1, str2 = str2, str1
    prev_memo = [0 for i in range(len(str2)+1)]
    cur_memo = [0 for i in range(len(str2)+1)]
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i == 0:
                cur_memo[j] = j
            elif j == 0:
                cur_memo[j] = i
            elif str1[i-1] == str2[j-1]:
                continue
            else:
                cur_memo[j] = 1 + min(prev_memo[j], cur_memo[j-1])

        prev_memo = cur_memo
        cur_memo = [0 for i in range(len(str2)+1)]

    return prev_memo[-1]


class MyTestCases(unittest.TestCase):

    def test_deletion_distance_base_case(self):
        self.assertEqual(deletion_distance_base('', 'test'), 4)
        self.assertEqual(deletion_distance_base('', ''), 0)

    def test_deletion_distance_recursive(self):
        self.assertEqual(deletion_distance_recursive('', 'test'), 4)
        self.assertEqual(deletion_distance_recursive('', ''), 0)
        self.assertEqual(deletion_distance_recursive('dog', 'frog'), 3)
        self.assertEqual(deletion_distance_recursive('some', 'some'), 0)
        self.assertEqual(deletion_distance_recursive('some', 'thing'), 9)
        self.assertEqual(deletion_distance_recursive('', ''), 0)

    def test_deletion_distance_2d_dp(self):
        self.assertEqual(deletion_distance_2d_dp('', 'test'), 4)
        self.assertEqual(deletion_distance_2d_dp('', ''), 0)
        self.assertEqual(deletion_distance_2d_dp('dog', 'frog'), 3)
        self.assertEqual(deletion_distance_2d_dp('some', 'some'), 0)
        self.assertEqual(deletion_distance_2d_dp('some', 'thing'), 9)
        self.assertEqual(deletion_distance_2d_dp('', ''), 0)

    def test_deletion_distance_1d_dp(self):
        self.assertEqual(deletion_distance_1d_dp('', 'test'), 4)
        self.assertEqual(deletion_distance_1d_dp('', ''), 0)
        self.assertEqual(deletion_distance_1d_dp('dog', 'frog'), 3)
        self.assertEqual(deletion_distance_1d_dp('some', 'some'), 0)
        self.assertEqual(deletion_distance_1d_dp('some', 'thing'), 9)
        self.assertEqual(deletion_distance_1d_dp('', ''), 0)