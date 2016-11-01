"""
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


class MyTestCases(unittest.TestCase):
    def test_common_factors_of_set(self):
        factors = common_factors_of_set([16, 32, 96])
        print(common_factors_of_set(factors, [2, 4]))
