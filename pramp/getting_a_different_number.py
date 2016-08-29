"""
input: arr
prop: size(n) where we have n unique ints
ex: [9,1, 4, 3]

any of the following
output: 0, 2, 5, 1000000
"""
import sys


def diff_number(arr):
    upper_bound = max(arr)  # n === upper_bound
    numbers_found = [False] * upper_bound
    for num in arr:
        numbers_found[num] = True
    for i, num in enumerate(numbers_found):
        if not num:
            return i
    if upper_bound == sys.maxsize:
        return -1
    return upper_bound + 1


[0, 1, 2]

#  i n
# [0, 1, 3, 4, 5, ... , max_int]  i=3 | n=3

# [0,1,...., x]
# x == max_value return -1
# x < max_value return x+1

# 0 - max_int


def diff_number(arr):
    if len(arr) == sys.maxsize:
        return -1
    for i, val in enumerate(arr):
        if i != val:
            return i
    return arr[-1] + 1

#    [0, 1, ..., 50,, MAX_INT]
#    len(n)


def diff_set_number(arr):
    if len(arr) == sys.maxsize:
        return -1
    contains = set()
    for val in arr:
        contains.add(val)
    for i in range(len(arr)):
        if i not in contains:
            return i
    return len(arr)