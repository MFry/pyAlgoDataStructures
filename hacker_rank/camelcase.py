"""
    Difficulty: *
    Code:       *

    Ref: https://www.hackerrank.com/challenges/camelcase
"""
import unittest


def camel_case(words):
    words_found = 1
    for letter in words:
        if letter.isupper():
            words_found += 1
    return words_found


class MyTestCases(unittest.TestCase):
    def test_camel_case(self):
        self.assertEqual(camel_case('saveChangesInTheEditor'), 5)


if __name__ == '__main__':
    s = input().strip()
    print(camel_case(s))
