"""
 Problem 20
 Data Structure: Stacks, optimization, design
"""
import unittest
from Algorithm_and_Data_Structures_Review.stack import Stack


class MaxStack(Stack):
    def __init__(self):
        self._max = Stack()
        Stack.__init__(self)

    def push(self, item):
        if not self._max:
            self._max.push(item)
        elif item >= self._max.peek():
            self._max.push(item)
        Stack.push(self, item)

    def pop(self):
        value = Stack.pop(self)
        if value == self._max.peek():
            self._max.pop()
        return value

    def get_max(self):
        return self._max.peek()


class MyTestCases(unittest.TestCase):
    def test_MaxStack(self):
        m_stack = MaxStack()
        for i in range(10):
            m_stack.push(i)
        for i in range(9, 0, -1):
            self.assertEqual(m_stack.get_max(), i)
            m_stack.pop()

        m_stack = MaxStack()
        m_stack.push(100)
        m_stack.push(5)
        m_stack.push(15)
        self.assertEqual(m_stack.get_max(), 100)
        m_stack.pop()
        m_stack.pop()
        self.assertEqual(m_stack.get_max(), 100)
