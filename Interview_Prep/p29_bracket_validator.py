"""

"""
import unittest


def bracket_validator(brackets):
    bracket_mapping = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    bracket_stack = []
    for bracket in brackets:
        if bracket in bracket_mapping:
            bracket_stack.append(bracket)
        else:
            must_close = bracket_stack[-1]
            if bracket_mapping[must_close] == bracket:
                bracket_stack.pop()
            else:
                return False
    return True


class MyTestCases(unittest.TestCase):
    def test_bracket_validator(self):
        test_brackets = "{[]()}"
        self.assertTrue(bracket_validator(test_brackets))
        test_brackets = "{[(])}"
        self.assertFalse(bracket_validator(test_brackets))
        test_brackets = "{[}"
        self.assertFalse(bracket_validator(test_brackets))
