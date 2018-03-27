"""
 Problem 22
 Delete a node from a singly-linked list, given only a variable pointing to that node.
 Linked List, Side-effects
"""
import unittest
from Algorithm_and_Data_Structures_Review.linkedlist import Node


def delete_node(node):
    """

    :param node:
    :type node: Node
    :return:
    """
    if not node.next_node:
        node.value = None
    else:
        node.value = node.next_node.value
        node.next_node = node.next_node.next_node
    node.next_node = None


class MyTestCases(unittest.TestCase):
    def test_delete_node(self):
        a = Node('A')
        a.next_node = Node('B')
        a.next_node.next_node = Node('C')
        b = a.next_node
        delete_node(b)
        self.assertEqual(b.value, 'C')
