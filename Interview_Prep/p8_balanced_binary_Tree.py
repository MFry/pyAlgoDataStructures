import unittest


"""
 Problem 8
"""


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
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
    level_traversal = [binary_tree]
    max_depth = 0
    min_depth = float('inf')
    while True:
        node_count = len(level_traversal)
        if node_count == 0:
            return max_depth, min_depth
        max_depth += 1
        while node_count > 0:
            current_node = level_traversal.pop(0)
            if not current_node.left and not current_node.right:
                if min_depth > max_depth:
                    min_depth = max_depth
            if current_node.left:
                level_traversal.append(current_node.left)
            if current_node.right:
                level_traversal.append(current_node.right)
            node_count -= 1


def superbalanced(binary_tree):
    """
        A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one
        Uses O(n) : a balanced full binary tree has l = (n+1)/2 leaf nodes
    :param binary_tree:
    :return:
    """

    max_depth, min_depth = find_max_depth(binary_tree)
    if max_depth - min_depth > 1:
        return False
    return True


class MyTestCases(unittest.TestCase):
    def test_superbalanced(self):
        bst_test = BinaryTreeNode(5)
        bst_test.insert_left(2)
        bst_test.left.insert_left(12)
        bst_test.left.insert_right(15)
        bst_test.left.left.insert_left(21)
        bst_test.left.left.insert_right(25)
        bst_test.insert_right(8)
        self.assertFalse(superbalanced(bst_test))
        bst_test.right.insert_left(33)
        bst_test.right.insert_right(66)
        bst_test.right.left.insert_left(31)
        bst_test.right.left.insert_right(32)
        bst_test.right.right.insert_left(65)
        bst_test.right.right.insert_right(67)
        # Complete the branch on the left side, right branch
        bst_test.left.right.insert_left(22)
        bst_test.left.right.insert_right(26)
        self.assertTrue(superbalanced(bst_test))
