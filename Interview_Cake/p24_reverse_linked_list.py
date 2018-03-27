"""

"""
import unittest
from Algorithm_and_Data_Structures_Review.linkedlist import Node


def reverse_list(head):
    """
        Reverses a linked list in place
    :param head:
    :return:
    """
    prev = None
    current = head
    while current:
        temp = current
        current = current.next_node
        temp.next_node = prev
        prev = temp
    return prev


class MyTestCases(unittest.TestCase):
    def test_reverse_list(self):
        test_head = Node(0)
        node = test_head
        for i in range(1, 10):
            node.next_node = Node(i)
            node = node._next_node
        reversed_list = reverse_list(test_head)
        self.assertEqual(reversed_list.value, 9)
        node = reversed_list
        for i in range(9, 0, -1):
            self.assertEqual(node.value, i)
            node = node.next_node
        # edge case test
        test_head = None
        reversed_list = reverse_list(test_head)
        self.assertEqual(reversed_list, None)
        test_head = Node(1)
        reversed_list = reverse_list(test_head)
        self.assertEqual(reversed_list.value, 1)
