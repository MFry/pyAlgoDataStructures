"""
    Ref: https://www.hackerrank.com/challenges/string-construction
"""


def construct(to_copy):
    used = set()
    cost = 0
    for letter in to_copy:
        if letter in used:
            continue
        used.add(letter)
        cost += 1
    return cost


print(construct('abab'))
