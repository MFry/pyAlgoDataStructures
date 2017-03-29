import unittest
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def check_binary_search_tree_(root):
    if not root:
        return True
    lower, upper = float('-inf'), float('inf')
    return (check_node(root, lower, upper))


def check_node(node, lower, upper):
    if not node:
        return True
    if node.data <= lower or node.data >= upper:
        return False
    return check_node(node.left, lower, node.data) and check_node(node.right, node.data, upper)


class MyTestCases(unittest.TestCase):
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def test_check_binary_search_tree(self):
        root = self.Node(50)
        root.left = self.Node(30)
        root.left.right = self.Node(60)
        root.left.left = self.Node(20)
        root.right = self.Node(80)
        root.right.left = self.Node(70)
        root.right.right = self.Node(90)
        self.assertFalse(check_binary_search_tree_(root))