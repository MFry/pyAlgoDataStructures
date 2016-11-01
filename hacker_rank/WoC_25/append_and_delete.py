"""
Ref: https://www.hackerrank.com/contests/w25/challenges/baby-step-giant-step
"""
import unittest


def continuous_similarity(s1, s2):
    size_to_check = min(len(s1), len(s2))
    for i in range(size_to_check):
        if s1[i] != s2[i]:
            return i
    return size_to_check


def changes_needed(s1, s2):
    continuous_length = continuous_similarity(s1, s2)
    return len(s1) + len(s2) - 2 * continuous_length, len(s1) + len(s2)


class MyTestCases(unittest.TestCase):
    def test_continuous_similarity(self):
        self.assertEqual(continuous_similarity('hackerhappy', 'hackerrank'), 6)
        self.assertEqual(changes_needed('hackerhappy', 'hackerrank')[0], 9)
        self.assertEqual(continuous_similarity('aba', 'aba'), 3)
        print(changes_needed('aba', 'aba'))
        print(changes_needed('appleton', 'applefig'))
