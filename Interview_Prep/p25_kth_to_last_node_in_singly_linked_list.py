"""

"""
import unittest
from Algorithm_and_Data_Structures_Review.linkedlist import Node


def kth_to_last_node(node, k):
    """

    :param node:
    :type node:Node
    :param k:
    :return:
    """
    leading_node = node
    for i in range(k):
        leading_node = leading_node.next_node
        if not leading_node:
            return None
    k_last_node = node
    while leading_node.next_node:
        leading_node = leading_node.next_node
        k_last_node = k_last_node.next_node
    return k_last_node


class MyTestCases(unittest.TestCase):
    def test_kth_to_last_node(self):
        test_head = Node(1)
        temp = test_head
        for i in range(10):
            temp.next_node = Node(i + 1)
            temp = temp.next_node
        k_th_node = kth_to_last_node(test_head, 3)
        self.assertEqual(k_th_node.value, 7)
        k_th_node = kth_to_last_node(k_th_node, 6)
        self.assertEqual(k_th_node, None)
