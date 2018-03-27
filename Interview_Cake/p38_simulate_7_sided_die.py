"""
    You have a function rand5() that generates a random integer from 1 to 5.
    Use it to write a function rand7() that generates a random integer from 1 to 7.
    rand5() returns each integer with equal probability. rand7() must also return each integer with equal probability.
"""
import unittest
import random


def rand5():
    return random.randrange(1, 6)


for i in range(25):
    print(rand5())


def rand7():
    roll1 = rand5()
    roll2 = rand5()

    while True:
        # [0-25]   [0-4] * 5  +  [0-4]   + 1
        outcome = (roll1 - 1) * 5 + (roll2 - 1) + 1
        if outcome <= 21:
            return outcome % 21 + 1
