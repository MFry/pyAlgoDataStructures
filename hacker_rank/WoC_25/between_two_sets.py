"""
gcd and lcm.
A fact that helped me -
If two numbers have no prime factors in common, the lowest common multiple will be equal to the product of the two numbers

Ref:
"""
import unittest


def common_factors_of_set(s, factors=set()):
    factors = set(factors)
    # find all factors for the smallest s
    to_factor = min(s)
    for i in range(1, to_factor + 1):
        if to_factor % i == 0:
            factors.add(i)
    s.remove(to_factor)
    for num in s:
        to_remove = set()
        for factor in factors:
            if num % factor != 0:
                to_remove.add(factor)
        factors = factors.difference(to_remove)
    return factors


def filter_by_factors(s, factors):
    s = set(s)
    to_delete = set()
    for num in s:
        for factor in factors:
            if num % factor != 0:
                to_delete.add(num)
                break
    return s.difference(to_delete)


class MyTestCases(unittest.TestCase):
    def test_common_factors_of_set(self):
        factors = common_factors_of_set([16, 32, 96])
        print(filter_by_factors(factors, [4, 2]))
        factors = common_factors_of_set([1])
        print(filter_by_factors(factors, [3, 5, 11]))
        factors = common_factors_of_set([3, 4])
        print(filter_by_factors(factors, [6]))
