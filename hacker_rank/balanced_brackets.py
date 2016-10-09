"""

"""
import unittest


def balanced_brackets(brackets):
    stack = []
    bracket_matching = {
        '{':'}',
        '[':']',
        '(':')'
    }
    valid_characters = {'{','}','[',']','(',')'}
    for bracket in brackets:
        if not valid_characters:
            raise Exception('Unrecognized Character')
        if bracket in bracket_matching:
            stack.append(bracket_matching[bracket])
        else:
            if len(stack) == 0:
                return False
            t = stack.pop()
            if t != bracket:
                return False
    return not stack


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input().strip()
        if balanced_brackets(s):
            print('YES')
        else:
            print('NO')
