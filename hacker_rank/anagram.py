"""

"""
import unittest


def anagram(w1, w2):
    if len(w1) != len(w2):
        return -1
    histogram = {}
    for letter in w1:
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram[letter] = 1
    min_changes = 0
    for letter in w2:
        if letter in histogram and histogram[letter] > 0:
            histogram[letter] -= 1
        else:
            min_changes += 1
    return min_changes


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        check = input().strip()
        print(anagram(check[:len(check)//2], check[len(check)//2:]))
