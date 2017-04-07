#!/bin/python3


# bisect - https://docs.python.org/3.6/library/bisect.html
# heapq - https://docs.python.org/3/library/heapq.html
from heapq import heappush, heappop
import unittest


class Heap:

    def __init__(self, max_heap=False):
        self.max_heap = max_heap
        self._heap = []

    def push(self, val):
        if self.max_heap:
            val *= -1
        heappush(self._heap, val)

    def pop(self):
        ret = heappop(self._heap)
        if self.max_heap:
            ret *= -1
        return ret

    def __len__(self):
        return len(self._heap)

    def __getitem__(self, key):
        ret = self._heap[key]
        if self.max_heap:
            ret *= -1
        return ret

    def __bool__(self):
        return bool(self._heap)

    def __iter__(self):
        self._i = -1
        return self

    def __next__(self):
        if self._i + 1 < len(self._heap):
            self._i += 1
            return self._heap[self._i]
        else:
            raise StopIteration

    def __str__(self):
        to_str = '['
        for val in self._heap:
            if self.max_heap:
                val *= -1
            to_str += ' ' + str(val)
        to_str += ' ]'
        return to_str


class RunningMedianContainer:

    def __init__(self):
        self.max_heap = Heap(max_heap=True)
        self.min_heap = Heap()

    def add_element(self, val):
        max_heap = self.max_heap
        min_heap = self.min_heap
        if not min_heap or min_heap[0] < val:
            min_heap.push(val)
        else:
            max_heap.push(val)
        self._rebalance()

    def _rebalance(self):
        large_heap = self.min_heap if len(self.min_heap) > len(self.max_heap) else self.max_heap
        small_heap = self.max_heap if len(self.max_heap) < len(self.min_heap) else self.min_heap
        if len(large_heap) - len(small_heap) > 1:
            small_heap.push(large_heap.pop())

    def get_median(self):
        large_heap = self.min_heap if len(self.min_heap) > len(self.max_heap) else self.max_heap
        small_heap = self.max_heap if len(self.max_heap) < len(self.min_heap) else self.min_heap
        if len(small_heap) == len(large_heap):
            return (small_heap[0]+large_heap[0])/2
        else:
            return large_heap[0]


class MyTestCases(unittest.TestCase):
    def test_running_median(self):
        medianContainer = RunningMedianContainer()
        medianContainer.add_element(1)
        self.assertEqual(1, medianContainer.get_median())
        medianContainer.add_element(2)
        self.assertEqual(1.5, medianContainer.get_median())
        medianContainer.add_element(3)
        self.assertEqual(2, medianContainer.get_median())
        medianContainer.add_element(4)
        self.assertEqual(2.5, medianContainer.get_median())


if __name__ == '__main__':
    n = int(input().strip())
    a = []
    runningMedianContainer = RunningMedianContainer()
    for _ in range(n):
        runningMedianContainer.add_element(int(input().strip()))
        print(runningMedianContainer.get_median())
