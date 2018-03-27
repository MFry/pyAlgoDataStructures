"""
    Difficulty: **
    Coding: *
"""
import unittest


def single_rifle_check(card_deck):
    if len(card_deck) != 52:
        raise Exception("We do not have a complete deck of cards")
    half_1 = 1
    half_2 = None
    for card in card_deck:
        if card == half_1:
            half_1 += 1
        elif not half_2:
            half_2 = card + 1
        elif half_2 == card:
            half_2 += 1
        else:
            return False
    return True


class MyTestCases(unittest.TestCase):
    def test_single_rifle_check(self):
        half1 = [i for i in range(1, 27)]
        half2 = [i for i in range(27, 53)]
        test_deck = []
        for i, j in zip(half1, half2):
            test_deck.append(i)
            test_deck.append(j)
        self.assertTrue(single_rifle_check(test_deck))
        test_deck = [1, 2, 3, 27, 28, 4, 29, 30, 5, 31, 6, 32, 7, 33, 8, 34, 9, 35, 10, 36, 11, 37, 12, 38, 13, 39, 14,
                     40, 15, 41, 16, 42, 17, 43, 18, 44, 19, 45, 20, 46, 21, 47, 22, 48, 23, 49, 24, 50, 25, 51, 26, 52]
        test_deck = []
        for i, j in zip(half1, half2):
            test_deck.append(j)
            test_deck.append(i)
        self.assertTrue(single_rifle_check(test_deck))
