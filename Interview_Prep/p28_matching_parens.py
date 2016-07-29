"""

"""
import unittest


def inefficient_find_matching_parenthesis(string, start):
    parenthesis_match = ['(']
    for i, character in enumerate(string[start + 1:]):
        if character == '(':
            parenthesis_match.append('(')
        elif character == ')':
            parenthesis_match.pop(0)
            if len(parenthesis_match) == 0:
                return start + 1 + i
    return -1


def find_matching_parenthesis(string, start):
    parenthesis_match = 1
    for i, character in enumerate(string[start + 1:]):
        if character == '(':
            parenthesis_match += 1
        elif character == ')':
            parenthesis_match -= 1
            if parenthesis_match == 0:
                return start + 1 + i
    return -1


class MyTestCases(unittest.TestCase):
    def test_find_matching_parenthesis(self):
        test_string = "Sometimes (when I nest them (my parentheticals)" \
                      " too much (like this (and this))) they get confusing"
        self.assertEqual(find_matching_parenthesis(test_string, 10), 79)
