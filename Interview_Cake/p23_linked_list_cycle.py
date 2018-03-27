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
            return True
    return False


class MyTestCases(unittest.TestCase):
    def test_contains_cycles(self):
        test_head = Node('A')
        test_node_b = Node('B')
        test_node_c = Node('C')
        test_node_d = Node('D')
        test_head.next_node = test_node_b
        test_node_b.next_node = test_node_c
        test_node_c.next_node = test_node_d
        test_node_d.next_node = test_node_b
        self.assertFalse(contains_cycle(test_head))
        test_node_d.next_node = test_node_d
        self.assertFalse(contains_cycle(test_head))
        test_node_d.next_node = test_node_c
        self.assertFalse(contains_cycle(test_head))
        test_node_d.next_node = None
        self.assertTrue(contains_cycle(test_head))
