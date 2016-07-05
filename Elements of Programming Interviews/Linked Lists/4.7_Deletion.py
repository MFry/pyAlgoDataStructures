import unittest
from linkedlist import LinkedList
from linkedlist import Node


def delete_node(l, node):
    """

    :param l: LinkedList contained the node to be deleted
    :type l: LinkedList
    :param node: Node to be deleted
    :type node: Node
    :return: Original LinkedList with the node deleted
    :rtype: LinkedList
    """
    if not l and node:
        return l
    current_node = l.head
    prev_node = None
    while current_node:
        if current_node == node:
            if current_node == l.head:
                l.head = current_node.next_node
            else:
                prev_node.next_node = current_node.next_node
            break
        prev_node = current_node
        current_node = current_node.next_node
    return l


class MyTestCases(unittest.TestCase):
    def test_delete_node(self):
        test_list = LinkedList()
        test_list.add(1)
        test_list = delete_node(test_list, test_list.head)
        self.assertTrue(test_list.head is None)
        for i in range(10):
            test_list.add(val=i)
        for node in test_list:
            if node.value == 2:
                delete = node
        test_list = delete_node(test_list, delete)
        self.assertFalse(test_list.get(delete.value))
