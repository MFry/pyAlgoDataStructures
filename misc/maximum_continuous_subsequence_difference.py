"""
    Ref: https://www.careercup.com/question?id=19286747
"""
import unittest


def get_right_left_difference(arr):
    l_start, l_stop, min = -1, -1, float('inf')
    r_start, r_stop, max = -1, -1, float('-inf')
    # find largest subsequence
    cur = 0
    for i, val in enumerate(arr):
        if cur + val > max:
            if r_stop + 1 != i or r_start < 0:
                r_start = i
            r_stop = i

