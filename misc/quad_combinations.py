"""
    Difficulty: ***
    Code: ****

    Given an array of numbers arr and a number S, find 4 different numbers in arr that sum up to S.

    Write a function that gets arr and S and returns an array with 4 indices of such numbers in arr,
     or null if no such combination exists.
    Explain and code the most efficient solution possible, and analyze its runtime and space complexity.

    Ref: http://stackoverflow.com/questions/2459653/how-to-find-smallest-substring-which-contains-all-characters-from-a-given-string


"""
import unittest


def smallest_substring(string, string_pattern):
    pattern_histogram = {}
    for character in string_pattern:
        if character in pattern_histogram:
            pattern_histogram[character] += 1
        else:
            pattern_histogram[character] = 1
    found_substring = {}
    minimum_size = 0
    start = 0
    end = -1

    for i, character in enumerate(string):
        if character in string_pattern:
            if character in found_substring:
                found_substring[character] = 0
            else:
                found_substring[character] += 1
            if found_substring[character] == pattern_histogram[character]:
                # check if we are done
                for key in pattern_histogram:
                    pass


class MyTestCases(unittest.TestCase):
    def test_quad_combinations(self):
        pass
