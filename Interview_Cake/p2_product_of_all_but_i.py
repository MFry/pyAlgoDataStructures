"""
    Difficulty: ***
    Code: **
    Problem 2
    Greedy
"""
import unittest


def get_products_of_all_ints_except_at_index(int_list):
    multiplied_list = [1] * len(int_list)
    multiple = 1
    for i, element in enumerate(int_list):
        multiplied_list[i] *= multiple
        multiple *= element
    multiple = 1
    for i, element in enumerate(reversed(int_list)):
        multiplied_list[-1 - i] *= multiple
        multiple *= element
    return multiplied_list


class MyTestCase(unittest.TestCase):
    def test_get_products_of_all_ints_except_at_index(self):
        to_multiply = [1, 2, 6, 5, 9]
        self.assertEqual(get_products_of_all_ints_except_at_index(to_multiply), [540, 270, 90, 108, 60])
        to_multiply = [1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(get_products_of_all_ints_except_at_index(to_multiply), to_multiply)
        to_multiply = [0, 1, 2, 6, 5, 9]
        print(get_products_of_all_ints_except_at_index(to_multiply))
