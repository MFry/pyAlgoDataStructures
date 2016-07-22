import unittest

"""
http://www.tutorialspoint.com/data_structures_algorithms/binary_search_tree.htm
"""


class TreeNode:
    def __init__(self, value):
        self._data = value
        self._parent = None

    @property
    def value(self):
        return self._data

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node

    def __str__(self):
        return '[' + str(self.value) + ']'


class BSTNode(TreeNode):
    def __init__(self, value):
        TreeNode.__init__(self, value)
        self._left = None
        self._right = None

    @property
    def left_node(self):
        """

        :return:
        :rtype: BSTNode
        """
        return self._left

    @left_node.setter
    def left_node(self, node):
        self._left = node

    @property
    def right_node(self):
        """

        :return:
        :rtype: BSTNode
        """
        return self._right

    @right_node.setter
    def right_node(self, node):
        self._right = node


class Tree:
    def __init__(self, node=None):
        """

        :param node:
        :type node: TreeNode
        """
        node.parent = None
        self._root = node

    @property
    def root(self):
        """

        :return:
        :rtype: TreeNode
        """
        return self._root


class BinarySearchTree(Tree):
    def insert(self, value=None, node=None):
        if value:
            to_insert = BSTNode(value)
        else:
            to_insert = node

        n = self.root
        while True:
            if n.value > to_insert.value:
                if not n.left_node:
                    to_insert.parent = n
                    n.left_node = to_insert
                    break
                else:
                    n = n.left_node
            else:
                if not n.right_node:
                    to_insert.parent = n
                    n.right_node = to_insert
                    break
                else:
                    n = n.right_node

    def delete(self, value):

        n = self.root
        while True:
            if n.value == value:
                # Case 1: No Children
                if not (n.left_node and n.right_node):
                    p = n.parent
                    if p.left_node and p.left_node.value == value:
                        n.parent.left_node = None
                        return n
                    else:
                        n.parent.right_node = None
                        return n
                        # Case 2: One Child

            if n.value > value:
                n = n.left_node
            else:
                n = n.right_node

    def __str__(self):
        out = ''
        nodes = []
        n = self.root
        nodes.append(n)
        depth = 0
        # [P]: X [D:] d [C:]{c1,c2}
        while nodes:
            t = []
            for n in nodes:
                if n.left_node:
                    t.append(n.left_node)
                if n.right_node:
                    t.append(n.right_node)
                out += str(n.value) + ' '
            out += '\n'
            nodes = t
        return out


test = BinarySearchTree(BSTNode(5))
test.insert(2)
test.insert(7)
test.insert(1)
test.insert(3)
test.insert(4)
print(test)
test.delete(4)
print(test)

test2 = BinarySearchTree(BSTNode(27))
test2.insert(35)
test2.insert(14)
test2.insert(42)
test2.insert(31)
test2.insert(10)
test2.insert(19)
print(test2)
# https://www.topcoder.com/community/data-science/data-science-tutorials/an-introduction-to-binary-search-and-red-black-trees/
