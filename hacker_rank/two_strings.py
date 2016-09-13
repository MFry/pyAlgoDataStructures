"""
 Ref: https://www.hackerrank.com/challenges/two-strings
"""
import unittest


def common_substring(a, b):
    sub_a = set()
    sub_b = set()
    for character in a:
        sub_a.add(character)
    for character in b:
        sub_b.add(character)
    if len(sub_a.intersection(sub_b)):
        return True
    return False


class MyTestCases(unittest.TestCase):
    def test_common_substring(self):
        self.assertTrue(common_substring('hello', 'world'))
        self.assertFalse(common_substring('hi', 'world'))

if __name__ is '__main__':
    total = int(input())
    for _ in range(total):
        a = input()
        b = input()
        if common_substring(a, b):
            print('YES')
        else:
            print('NO')