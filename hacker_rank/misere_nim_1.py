"""
 Ref: https://www.hackerrank.com/challenges/misere-nim-1
 Wikipedia: https://en.wikipedia.org/wiki/Nim
 Solution hint: http://mathoverflow.net/questions/71802/analysis-of-misere-nim
"""
import unittest


def misere_nim(piles):
    xor_piles = 0
    for pile in piles:
        xor_piles ^= pile
    if xor_piles == 0:
        if max(piles) > 1:
            return 'Second'
    elif xor_piles == 1:
        if max(piles) <= 1:
            return 'Second'
    return 'First'


class MyTestCases(unittest.TestCase):
    def test_misere_nim(self):
        piles = [1, 1]
        self.assertEqual(misere_nim(piles), 'First')
        piles = [2, 1, 3]
        self.assertEqual(misere_nim(piles), 'Second')
