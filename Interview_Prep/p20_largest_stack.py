"""
 Problem 20
"""
import unittest
from Algorithm_and_Data_Structures_Review.stack import Stack


class MaxStack(Stack):
    def __init__(self):
        self._max = []
        Stack.__init__(self)

    def push(self, item):
        if item > self._max:
            self._max.append(item)
        Stack.push(self, item)

    def pop(self):
        value = Stack.pop(self)
        if value == self._max[-1]:
            self._max.pop()
        return value

    def get_max(self):
        return self._max[-1]


class MyTestCases(unittest.TestCase):
    def test_MaxStack(self):
        m_stack = MaxStack
        for i in range(10):
            m_stack.push(i)
        for i in range(10, 0, -1):
            pass
