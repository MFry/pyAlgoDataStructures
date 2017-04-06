#!/bin/python3

import sys
# bisect - https://docs.python.org/3.6/library/bisect.html
# heapq - https://docs.python.org/3/library/heapq.html
from heapq import heappush


class RunningMedianContainer:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def _add_to_max_heap(self, val):
        val *= -1
        heappush(self.max_heap, val)

    def _get_from_max_heap(self):
        return self.max_heap[0] * -1

    def add_element(self, val):
        max_heap = self.max_heap
        min_heap = self.min_heap
        if len(max_heap) > len(min_heap):
            heappush(min_heap, val)


if __name__ == '__main__':
    n = int(input().strip())
    a = []
    for _ in range(n):
        a.append(int(input().strip()))
