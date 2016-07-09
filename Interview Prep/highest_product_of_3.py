import unittest
from functools import reduce
from operator import mul

"""
    Problem 3
    Greedy
"""


def highest_product(list_of_ints):
    largest_numbers = [float('-inf')] * 3
    smallest_negative = [float('inf')] * 2
    min_largest = min(largest_numbers)
    for item in list_of_ints:
        if item > min_largest:
            largest_numbers.remove(min_largest)
            largest_numbers.append(item)
            min_largest = min(largest_numbers)
        if item < 0:
            max_smallest = max(smallest_negative)
            if item < max_smallest:
                smallest_negative.remove(max_smallest)
                smallest_negative.append(item)
    largest_negative_2_product = reduce(mul, smallest_negative)
    largest_product = reduce(mul, largest_numbers)
    if largest_product > 0 and largest_negative_2_product > 0:
        largest_numbers = sorted(largest_numbers)
        largest = largest_numbers[-1]
        second_largest = largest_numbers[-2]
        if largest_negative_2_product > largest * second_largest:
            return largest_negative_2_product * largest
    return largest_product


class MyTestClass(unittest.TestCase):
    def test_highest_product(self):
        list_of_ints = [-10, -10, 1, 3, 2]
        self.assertEqual(highest_product(list_of_ints), 300)
        list_of_ints = [1, 10, -5, 1, -100]
        self.assertEqual(highest_product(list_of_ints), 5000)
        list_of_ints = [-100000, 5, 4, 1]
        self.assertEqual(highest_product(list_of_ints), 20)
        list_of_ints = [-8, -1, -3, -10000]
        self.assertEqual(highest_product(list_of_ints), -24)
