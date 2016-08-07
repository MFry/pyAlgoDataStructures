"""
    Difficulty: ****
    Code:       *****
Given a set T of characters and a string S, find the minimum window in S which will contain all the characters in T

S = “ADOBECODEBANC”
T = “ABC”

Minimum window is “BANC”.

Ref:
    http://articles.leetcode.com/finding-minimum-window-in-s-which

    http://stackoverflow.com/questions/2459653/how-to-find-smallest-substring-which-contains-all-characters-from-a-given-string
"""
import unittest


def is_palindrome(to_check, start, end):
    while start < end:
        if to_check[start] != to_check[end]:
            return False
        start += 1
        end -= 1
    return True


def palindrome_creation(letters):
    start = 0
    end = len(letters) - (1 + start)
    while start < end:
        end = len(letters) - (1 + start)
        if letters[start] == letters[end]:
            start += 1
            continue
        if is_palindrome(letters, start+1, end):
            return start
        else:
            return end

    return -1