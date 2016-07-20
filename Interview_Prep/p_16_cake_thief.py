"""
    Each type of cake has a weight and a value, stored in a tuple with two indices:

    0: An integer representing the weight of the cake in kilograms
    1: An integer representing the monetary value of the cake in British pounds
    Problem 16
"""
import unittest
import functools


def sort_cakes(cake1, cake2):
    if cake1[0] == 0:
        if cake1[0] > 0:
            raise Exception("Infinite pounds generated")
        else:
            return -1
    if cake2[0] == 0:
        if cake2[1] > 0:
            raise Exception("Infinite pounds generated")
        else:
            return -1
    if cake1[0]*cake2[1] > cake2[0]*cake1[1]:
        return 1
    else:
        return -1


def greedy_max_duffel_bag_value(cake_tuples, capacity):
    cake_tuples.sort(key=functools.cmp_to_key(sort_cakes))
    british_pounds_made = 0
    for cake_tuple in cake_tuples:
        cakes_stolen = capacity // cake_tuple[0]
        british_pounds_made += cake_tuple[1] * cakes_stolen
        capacity -= cake_tuple[0] * cakes_stolen
    return british_pounds_made


def max_duffel_bag_value(cake_tuples, capacity):
    possible_pounds_stolen = [0] * capacity + 1
    cake_tuples.sort(key=lambda x: x[0])
    # check if weight is 0 and money > 0, return infinity
    best_profit_made = 0
    for cake_tuple in cake_tuples:
        for pounds_stolen_per_weight in possible_pounds_stolen[cake_tuple[0]:]:
            # check if we can make better profit at the given weight than what we have so far
            pass
    return best_profit_made


class MyTestCases(unittest.TestCase):
    def test_max_duffel_bag_value(self):
        cake_tuples = [(7, 160), (3, 90), (2, 15)]
        capacity = 20
        self.assertEqual(max_duffel_bag_value(cake_tuples, capacity), 555)
