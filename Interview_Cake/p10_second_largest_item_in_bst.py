"""
 Problem 10
 Greedy, Tree
"""
import unittest
from Algorithm_and_Data_Structures_Review.binary_search_tree import BinaryTreeNode


def find_largest_value(bst):
    current_node = bst
    answer = None
    while current_node:
        answer = current_node.value
        current_node = current_node.right
    return answer


def find_second_largest_value_in_bst(bst):
    current_node = bst
    prev_node = None
    if not current_node.right:
        return current_node.left
    while current_node:
        prev_node = bst
        if not current_node.right and current_node.left:
            return find_largest_value(current_node.left)
        current_node = current_node.right
    return prev_node.value


class MyTestCases(unittest.TestCase):
    def test_find_second_largest_in_bst(self):
        bst = BinaryTreeNode(10)
        bst.insert_left(5)
        bst.insert_right(12)
        self.assertEqual(find_second_largest_value_in_bst(bst), 10)
        bst.right.insert_left(11)
        bst.right.insert_right(15)
        self.assertEqual(find_second_largest_value_in_bst(bst), 12)
        bst.right.right.insert_right(25)
        self.assertEqual(find_second_largest_value_in_bst(bst), 15)
