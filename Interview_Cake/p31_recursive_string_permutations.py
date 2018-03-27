"""
    Write a recursive function for generating all permutations of an input string. Return them as a set.
    Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.

    To start, assume every character in the input string is unique.

    Your function can have loops—it just needs to also be recursive.
"""
import unittest


def all_permutations(string_list, permutations_set=None):
    permutations_set = permutations_set if permutations_set else set(list(string_list.pop(0)))
    if len(string_list) <= 0:
        return permutations_set
    else:
        permuted_set = set()
        character = string_list.pop(0)
        while permutations_set:
            to_permute = permutations_set.pop()
            for i in range(len(to_permute)):
                permuted_set.add(to_permute[:i] + character + to_permute[i:])
            permuted_set.add(to_permute + character)
    return all_permutations(string_list, permuted_set)


class MyTestCases(unittest.TestCase):

    def test_all_permutations(self):
        print(all_permutations(list('abc')))
        print(all_permutations(list('cats')))
        # abc
        # acb
        # bca
        # bac
        # cab
        # cba
        pass
