"""
    Very basic implementation of a linked list
"""
import unittest


class Node:
    def __init__(self, value):
        self._value = value
        self._next_node = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, x):
        self._value = x

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        self._next_node = node

    def __str__(self):
        out = '['+str(self.value)+']'
        return out


class LinkedList:
    def __init__(self, val=None):
        self._head = None
        self._tail = None
        self._length = 0
        if val:
            self.add(val)

    @property
    def tail(self):
        """

        :return: Returns the last node in the linked list
        :rtype: Node
        """
        return self._tail

    @tail.setter
    def tail(self, node):
        self._tail = node

    @property
    def head(self):
        """

        :return: Linked List Starting Value
        :rtype: Node
        """
        return self._head

    @head.setter
    def head(self, node):
        self._head = node

    def add(self, val=None, node=None):
        if val is not None:
            n = Node(val)
        elif node:
            n = node
        if not self.head:
            self._set_first(n)
        else:
            self._add(n)

    def _set_first(self, node):
        self._head = node
        self._tail = self._head
        self._length += 1

    def _add(self, node):
        self.tail.next_node = node
        self.tail = node
        self._length += 1

    def get(self, val):
        found_node = None
        for node in self:
            if node.value == val:
                found_node = node
                break
        return found_node

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        next_node = self._current
        self._current = self._current.next_node
        return next_node

    def __len__(self):
        return self._length

    def __str__(self):
        out = ''
        n = self.head
        while n:
            out += str(n)
            out += ' - '
            n = n.next_node
        return out


class MyTestCase(unittest.TestCase):
    def test_LinkedList(self):
        t = LinkedList()
        self.assertEqual(t.head, None)
        t.add(5)
        self.assertEqual(t.head.value, 5)
        for i in range(10):
            t.add(i)
        self.assertEqual(str(t), '[5] - [0] - [1] - [2] - [3] - [4] - [5] - [6] - [7] - [8] - [9] - ')
        self.assertEqual(len(t), 11)
        self.assertEqual(t.get(5).value, 5)


if __name__ == '__main__':
    unittest.main()
