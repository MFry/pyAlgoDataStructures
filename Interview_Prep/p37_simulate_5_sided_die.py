"""
    You have a function rand7() that generates a random integer from 1 to 7.
    Use it to write a function rand5() that generates a random integer from 1 to 5.
    rand7() returns each integer with equal probability. rand5() must also return each integer with equal probability.
"""
import unittest
import random


def rand7():
    return random.randrange(1, 7)


def rand5():
    r = rand7()
    if r > 5:
        r = rand7()
    return r


class MyTestCases(unittest.TestCase):
    def test_rand5(self):
        pass
