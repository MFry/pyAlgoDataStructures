"""
 Ref: https://www.hackerrank.com/challenges/insertionsort2/submissions/code/28381173
"""
import unittest


def visual_insertion_sort(arr):
    for i in range(1, len(arr)):
        to_sort = arr[i]
        j = i
        while j > 0:
            if to_sort > arr[j - 1]:
                break
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = to_sort
        print(' '.join([str(i) for i in arr]))
    return arr


_ = input()
arr = [int(i) for i in input().split()]
visual_insertion_sort(arr)
