"""
 Given a sorted array of unknown length and a number to search for, return the index of the number in the array.
 Accessing an element out of bounds throws exception. If the number occurs multiple times, return the index of
 any occurrence. If it isn’t present, return -1.

 link: http://www.ardendertat.com/2011/11/21/programming-interview-questions-17-search-unknown-length-array/
"""
import unittest


class UnboundArray:
    def __init__(self, *args):
        self._length = None
        self._data = []
        for value in args:
            self._data.append(value)

    def _get_value(self, index):
        if self._length < index:
            raise IndexError
        else:
            return self._data[index]

    def __getitem__(self, item):
        return self._get_value(item)


def find_element_in_unknown_sized_array(unknown_sized_array, unknown_value):
    upper_bound_guess = 100
    lower_bound = 0
    mid_point = 50
    # find upper bound using binary search
    while True:
        try:
            val = unknown_sized_array[mid_point]
            if val == unknown_value:
                return mid_point
            elif val > unknown_value:
                upper_bound_guess = mid_point - 1
                # we found an upper bound
                break
            else:
                lower_bound = mid_point + 1
                upper_bound_guess *= 2
        except IndexError:
            upper_bound_guess *= .75
    # find value
    while upper_bound_guess >= lower_bound:
        val = unknown_sized_array[mid_point]
        if val == unknown_value:
            return mid_point
        elif val > unknown_value:
            upper_bound_guess = mid_point - 1
        else:
            lower_bound = mid_point + 1
    return -1


class MyTestCases(unittest.TestCase):
    def test_find_element_in_unknown_sized_array(self):
        pass
