"""
 Problem 13

"""
import unittest


def find_rotation(word_list):
    lower_bound = 0
    upper_bound = len(word_list) - 1
    while True:
        split_point = (upper_bound + lower_bound) // 2
        if word_list[split_point] < word_list[upper_bound]:
            upper_bound = split_point
        if word_list[split_point] > word_list[lower_bound]:
            lower_bound = split_point
        if upper_bound == lower_bound:
            return -1
        if upper_bound - lower_bound == 2:
            return lower_bound + 1


class MyTestCase(unittest.TestCase):
    def test_find_rotation(self):
        words = ['ptomeaic',
                 'retrograde',
                 'supplant',
                 'undulate',
                 'xenoepist',
                 'asymptote',
                 'babka',
                 'banoffee',
                 'engender',
                 'karpatka',
                 'othellolagkage']
        self.assertEqual(find_rotation(words), 4)
        words = ['a',
                 'b',
                 'c',
                 'd',
                 'e',
                 'f']
        self.assertEqual(find_rotation(words), -1)
