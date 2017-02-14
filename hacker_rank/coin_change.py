"""
Ref: https://www.hackerrank.com/challenges/coin-change
"""
import unittest


# Incorrect
def change_permutations(coins, amount):
    change_combinations = [0] * (amount + 1)
    change_combinations[0] = 0
    coins.sort(reverse=True)
    for coin in coins:
        change_combinations[coin] += 1
        combi_start = coin * 2
        while combi_start < len(change_combinations):
            i = coin * 2
            while i < len(change_combinations):
                change_combinations[i] += 1
                i += coin
            combi_start += coin
    return change_combinations[amount]


class MyTestCases(unittest.TestCase):
    def test_change_permutations(self):
        self.assertEqual(change_permutations([1, 2, 3], 4), 4)
        self.assertEqual(change_permutations([2, 5, 3, 6], 10), 5)


if __name__ == '__main__':
    amount, total_coin = [int(i) for i in input().split()]
    coins = [int(i) for i in input().split()]
