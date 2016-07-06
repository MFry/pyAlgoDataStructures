import unittest
"""
Implement queue using two stacks and O(1) additional space
"""


class StacksSimulatedQueue:

    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    @staticmethod
    def _swap_stacks(full_stack, empty_stack):
        while len(full_stack) > 0:
            empty_stack.append(full_stack.pop())
        return full_stack, empty_stack

    def enqueue(self, x):
        self._stack1.append(x)

    def dequeque(self):
        if len(self._stack2) == 0:
            self._stack1, self._stack2 = self._swap_stacks(self._stack1, self._stack2)
        return self._stack2.pop()




class MyTestCase(unittest.TestCase):
    def test_StacksSimulatedQueue(self):
        test = StacksSimulatedQueue()
        test.enqueue(5)
        self.assertEqual(test.dequeque(), 5)
        test.enqueue(6)
        test.enqueue(7)
        self.assertEqual(test.dequeque(), 6)
