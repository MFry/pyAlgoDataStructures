"""
    ref: https://www.hackerrank.com/challenges/kangaroo
"""

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]


def kangaroo_meetup(x1, v1, x2, v2):
    dist = x1 - x2
    movement = v1 - v2
    if movement > 0 and dist % movement == 0:
        return "YES"
    else:
        return "NO"


print(kangaroo_meetup(x1, v1, x2, v2))
