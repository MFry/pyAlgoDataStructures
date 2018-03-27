"""
    Difficulty: ***
    Coding: **

  Ref: Fisher-Yates shuffle
"""
import unittest
import random


def in_place_shuffle(arr):
    insert_point = len(arr) - 1
    if insert_point < 1:
        return arr
    while insert_point > 0:
        i = random.randrange(0, insert_point + 1)
        arr[i], arr[insert_point] = arr[insert_point], arr[i]
        insert_point -= 1
    return arr


class MyTestCases(unittest.TestCase):
    def test_in_place_shuffle(self):
        arr = [i for i in range(11)]
        print(in_place_shuffle(arr))
        i = 0
        while i != 10:
            i = random.randrange(0, 11)
