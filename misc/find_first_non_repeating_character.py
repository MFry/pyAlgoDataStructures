"""
Given a string, find its first non-repeating character
Given a string, find the first non-repeating character in it.
For example, if the input string is “GeeksforGeeks”, then output
 should be ‘f’ and if input string is “GeeksQuiz”, then output should be ‘G’.
"""
import unittest


def first_none_repeating_character(string):
    single_occurrence = {}
    for i, character in enumerate(string):
        if character in single_occurrence:
            single_occurrence.pop(character)
        else:
            single_occurrence[character] = i
    for key in sorted(single_occurrence.items(), key=lambda x: x[1]):
        return key[0]
    return None


class MyTestCases(unittest.TestCase):
    def test_first_none_repeating_character(self):
        test_str = 'geeksforgeeks'
        self.assertEqual(first_none_repeating_character(test_str), 'f')
