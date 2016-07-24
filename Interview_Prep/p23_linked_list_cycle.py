"""
 Problem 23

"""
import unittest
from Algorithm_and_Data_Structures_Review.linkedlist import Node


def contains_cycle(head):
    """

    :param head: First node in a single-linked list
    :type head: Node
    :return: A boolean whether the list contains cycles
    """
    fast_node = head
    slow_node = head
    while fast_node and fast_node.next_node:
        fast_node = fast_node.next_node.next_node
        slow_node = slow_node.next_node
        if slow_node == fast_node:
            return False
    return True


class MyTestCases(unittest.TestCase):
    def test_contains_cycles(self):
        pass