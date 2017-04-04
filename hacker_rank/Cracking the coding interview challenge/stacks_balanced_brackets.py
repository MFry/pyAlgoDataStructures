# high performance stack
from collections import deque
import unittest


def is_matched(expression):
    if len(expression) % 2 != 0:
        return False
    stack = deque()
    brackets = {')': '(',
                ']': '[',
                '}': '{'}
    for bracket in expression:
        if bracket in brackets:
            if len(stack) == 0 or stack[-1] != brackets[bracket]:
                return False
            stack.pop()
        else:
            stack.append(bracket)

    if len(stack) > 0:
        return False
    return True


class MyTestCases(unittest.TestCase):
    def test_is_matched(self):

        t1 = '{[()]}'
        self.assertTrue(is_matched(t1))
        t2 = '{[(])}'
        t3 = '{{[[(())]]}}'


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression):
        print("YES")
    else:
        print("NO")
