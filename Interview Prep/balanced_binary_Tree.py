import unittest

"""
 Problem 8
"""


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def superbalanced(binary_tree):
    """
        A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one
    :param binary_tree:
    :return:
    """
    pass


class MyTestCases(unittest.TestCase):
    def test_superbalanced(self):
        pass
