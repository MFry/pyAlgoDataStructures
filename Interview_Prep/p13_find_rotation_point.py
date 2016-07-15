"""
 Problem 13

"""
import unittest


def find_rotation(word_list):
    lower_bound = 0
    upper_bound = len(word_list) - 1
    fird_word = word_list[0]

    while lower_bound < upper_bound:
        mid_point = lower_bound + (upper_bound-lower_bound) // 2
        if word_list[lower_bound] < word_list[mid_point]:
            lower_bound = mid_point
        else:
            upper_bound = mid_point
        if lower_bound + 1 == upper_bound:
            if word_list[lower_bound] < word_list[upper_bound]:
                return -1
            return lower_bound


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
        words = ['g',
                 'a',
                 'b',
                 'c',
                 'd',
                 'e',
                 'f']
        self.assertEqual(find_rotation(words), 0)
        words = ['a',
                 'b',
                 'c',
                 'd',
                 'e',
                 'f']
        self.assertEqual(find_rotation(words), -1)
