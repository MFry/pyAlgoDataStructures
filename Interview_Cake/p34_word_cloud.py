"""
    Difficulty: **
    Code: ****
    Note: In python, regex is faster for many of the operations below
    Ref: http://stackoverflow.com/a/1277047
"""

import unittest
import string


def generate_word_histogram(large_string):
    large_string += ' '
    histogram = {}
    start = 0
    for i in range(len(large_string)):
        char_check = large_string[i].strip().replace('.', '')
        if start is None and char_check:
            start = i
        if start is not None and not char_check:
            t = ''.join(filter(str.isalnum, large_string[start:i]))
            t = t.lower()
            if t in histogram:
                histogram[t] += 1
            else:
                histogram[t] = 1
            start = None
    return histogram


class MyTestCases(unittest.TestCase):
    def test_generate_word_histogram(self):
        test_string = 'After beating the eggs, Dana read the next step:'
        # print(generate_word_histogram(test_string))
        test_string = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."
        print(generate_word_histogram(test_string))
