"""
Problem 5
Dynamic Programming
"""
import unittest


def coin_permutations(amount, coins):
    possible_denominations = [0] * (amount + 1)
    possible_denominations[0] = 1

    for coin in coins:
        for i, _ in enumerate(possible_denominations):
            change = i - coin
            if change >= 0:
                possible_denominations[i] += possible_denominations[change]

    return possible_denominations[amount]


class MyTestCases(unittest.TestCase):
    def test_coin_permutations(self):
        coins = [1, 2, 3]
        amount = 4
        self.assertEqual(coin_permutations(amount, coins), 4)
        self.assertEqual(coin_permutations(amount + 1, coins), 5)
