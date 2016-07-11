import unittest

"""
Problem 5
Greedy
"""


def coin_permutations(amount, coins):

    possible_denominations = [0] * (len(amount)+1)

    for coin in coins:
        for i, _ in enumerate(possible_denominations):
            # TODO: Complete
            # answer += num_ways(amount_remaining, number of ways)
            pass

    return possible_denominations[amount+1]


