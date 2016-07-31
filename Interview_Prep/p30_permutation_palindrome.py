"""
Write an efficient function that checks whether any permutation of an input string is a palindrome.
Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
"""
import unittest


def permutation_palindrome(string):
    unpaired_character = set()
    for character in string:
        if character in unpaired_character:
            unpaired_character.remove(character)
        else:
            unpaired_character.add(character)
    return len(unpaired_character) < 2


class MyTestCases(unittest.TestCase):
    def test_permutation_palindrome(self):
        self.assertTrue(permutation_palindrome('civic'))
        self.assertTrue(permutation_palindrome('ivicc'))
        self.assertFalse(permutation_palindrome('civil'))
        self.assertFalse(permutation_palindrome('livci'))