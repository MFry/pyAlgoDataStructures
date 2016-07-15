import unittest

"""
Notes
In Order Traversal http://articles.leetcode.com/binary-search-tree-in-order-traversal
Post Order Traversal: http://articles.leetcode.com/binary-tree-post-order-traversal
Tree height:
"""


class BinaryTreeNode:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    def insert_left(self, value):
        """

        :param value:
        :return:
        :rtype : BinaryTreeNode
        """
        self._left = BinaryTreeNode(value)
        return self._left

    def insert_right(self, value):
        """

        :param value:
        :return:
        :rtype : BinaryTreeNode
        """
        self._right = BinaryTreeNode(value)
        return self._right

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        """
         :return:
         :rtype : BinaryTreeNode
        """
        return self._left

    @left.setter
    def left(self, bst_node):
        self._left = bst_node

    @property
    def right(self):
        """

        :return:
        :rtype : BinaryTreeNode
        """
        return self._right

    @right.setter
    def right(self, bst_node):
        self._right = bst_node


def find_max_depth(binary_tree):
    current_tree_level = [binary_tree]
    max_depth = 0
    while True:
        node_count = len(current_tree_level)
        if node_count == 0:
            return max_depth
        max_depth += 1
        while node_count > 0:
            current_node = current_tree_level.pop(0)
            if current_node.left:
                current_tree_level.append(current_node.left)
            if current_node.right:
                current_tree_level.append(current_node.right)
            node_count -= 1
    return max_depth


def in_order_traversal(binary_search_tree):
    """

    :param binary_search_tree:
    :type binary_search_tree: BinaryTreeNode
    :return:
    """
    out = ''
    nodes_to_check = [binary_search_tree]
    while len(nodes_to_check) > 0:
        current_node = nodes_to_check.pop(0)
        if current_node:
            out += str(current_node.value) + ' '
            nodes_to_check.append(current_node.left)
            nodes_to_check.append(current_node.right)
    return out


def pre_order_traversal(binary_search_tree):
    """

    :param binary_search_tree:
    :type binary_search_tree: BinaryTreeNode
    :return:
    """
    out = ''
    traversal_queue = [binary_search_tree]
    while len(traversal_queue) > 0:
        current_node = traversal_queue.pop()
        if current_node is not None:
            out += str(current_node.value) + ' '
            traversal_queue.insert(0, current_node.left)
            traversal_queue.insert(0, current_node.right)
    return out


def post_order_traversal(binary_search_tree):
    out = ''
    traversal_queue = [binary_search_tree]
    output_stack = []
    while len(traversal_queue) > 0:
        pass


class MyTestCases(unittest.TestCase):
    def test_in_order_traversal(self):
        bst_test = BinaryTreeNode(1)
        bst_test.insert_left(2)
        bst_test.insert_right(3)
        self.assertEqual(in_order_traversal(bst_test), '1 2 3 ')
        bst_test.left.insert_left(4)
        bst_test.left.insert_right(5)
        self.assertEqual(in_order_traversal(bst_test), '1 2 3 4 5 ')
        bst_test.right.insert_right(6)
        bst_test.right.right.insert_right(7)
        self.assertEqual(in_order_traversal(bst_test), '1 2 3 4 5 6 7 ')
        print(pre_order_traversal(bst_test))

    def test_max_depth(self):
        bst_test = BinaryTreeNode(1)
        bst_test.insert_left(2)
        bst_test.insert_right(3)
        bst_test.left.insert_left(4)
        bst_test.left.insert_right(5)
        bst_test.right.insert_right(6)
        bst_test.right.right.insert_right(7)
        self.assertEqual(find_max_depth(bst_test), 4)
