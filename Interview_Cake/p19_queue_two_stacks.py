"""
 Problem: 19
 Data Structures: Stack, Queue
"""
import unittest


class Queue:
    def __init__(self):
        self._input_stack = []
        self._output_stack = []

    def enqueue(self, val):
        self._input_stack.append(val)

    def dequeue(self):
        if len(self._output_stack) == 0:
            while len(self._input_stack):
                self._output_stack.append(self._input_stack.pop())
        return self._output_stack.pop()


class MyTestCases(unittest.TestCase):
    def test_Queue(self):
        q = Queue()
        for i in range(10):
            q.enqueue(i)
        self.assertEqual(q.dequeue(), 0)
        q.dequeue()
        q.dequeue()
        q.enqueue(25)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
