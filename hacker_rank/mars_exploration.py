"""
    Difficulty: *
    Code:       *
    Ref: https://www.hackerrank.com/challenges/mars-exploration
"""
import unittest


def sos_decrypt(s):
    altered = 0
    message = ['S', 'O', 'S']
    for i, letter in enumerate(s):
        if message[i % 3] != letter:
            altered += 1
    return altered


class MyTestCases(unittest.TestCase):
    def test_sos_decrypt(self):
        s = 'SOSSPSSQSSOR'
        self.assertEqual(sos_decrypt(s), 3)
        s = 'SOSSOT'
        self.assertEqual(sos_decrypt(s), 1)
