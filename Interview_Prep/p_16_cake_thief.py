"""
    Each type of cake has a weight and a value, stored in a tuple with two indices:

    0: An integer representing the weight of the cake in kilograms
    1: An integer representing the monetary value of the cake in British pounds
    Problem 16
"""
import unittest


def sort_cakes(cake1, cake2):
    if cake1[0] == 0:
        if cake1[1] > 0:
            return 1
        else:
            return -1
    if cake2[0] == 0:
        if cake2[1] > 0:
            return 1
        else:
            return -1
    if cake1[0]*cake2[1] > cake2[0]*cake1[1]:
        return 0
    else:
        return 0


def max_duffel_bag_value(cake_tuples, capacity):
    cake_tuples.sort(key=sort_cakes)
    pass



# [(7, 160), (3, 90), (2, 15)]