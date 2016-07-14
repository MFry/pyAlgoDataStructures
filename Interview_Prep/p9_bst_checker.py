"""
 Problem 9
 Greedy/Divide and Conquer, Tree
"""
import unittest
from Algorithm_and_Data_Structures_Review.binary_search_tree import BinaryTreeNode


def binary_search_tree_check(bst):
    node_bounds_stack = [(bst, float('inf'), float('-inf'))]
    while len(node_bounds_stack):
        current_node, upper_bound, lower_bound = node_bounds_stack.pop()
        if current_node.value > upper_bound or current_node.value < lower_bound:
            return False
        if current_node.left:
            node_bounds_stack.append((current_node.left, current_node.value, lower_bound))
        if current_node.right:
            node_bounds_stack.append((current_node.right, upper_bound, current_node.value))
    return True


def binary_search_tree_check2(bst):
    """
        Breath First Search implementation that takes every element and ensures it is sorted
        Time: O(n)
        Space: O(n)
    :param bst:
    :return:
    """
    node_queue = [bst]
    values = []
    while len(node_queue) > 0:
        current_node = node_queue.pop(0)
        values.append(current_node.value)
        if current_node.left:
            node_queue.append(current_node.left)
        if current_node.right:
            node_queue.append(current_node.right)
    prev = values[0]
    for value in values[1:]:
        if value < prev:
            return False
        prev = value
    return True


class MyTestCases(unittest.TestCase):
    def test_binary_search_tree_check(self):
        bst = BinaryTreeNode(50)
        bst.insert_left(30)
        bst.insert_right(80)
        bst.left.insert_left(20)
        bst.left.insert_right(60)
        bst.right.insert_left(70)
        bst.right.insert_right(90)
        self.assertTrue(binary_search_tree_check(bst) == binary_search_tree_check2(bst))
