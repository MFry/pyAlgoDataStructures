"""
    Very basic implementation of a linked list
"""


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
        if val:
            self._set_first(val)
        else:
            self._head = None
            self._tail = None
            self._length = 0

    def _set_first(self, val):
        self._head = Node(val)
        self._tail = self._head
        self._length = 1

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

    def add(self, val):
        n = Node(val)
        if not self.head:
            self._set_first(val)
        else:
            self.tail.next_node = n
            self.tail = n
            self._length += 1

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
