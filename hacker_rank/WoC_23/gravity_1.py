"""
 Name: Gravity Tree

 Ref: https://www.hackerrank.com/contests/w23/challenges/gravity-1
"""
import unittest


def construct_tree(nodes, node_connections):
    tree = {}
    for node in range(1, nodes + 1):
        tree[node] = []
    for i, conn in enumerate(node_connections, 1):
        tree[conn].append(i + 1)
    return tree


def gravity_tree(tree, u, v):
    distances = []
    to_traverse = tree[v]
    dist = 1
    temp = []
    while to_traverse:
        cur = to_traverse.pop(0)
        distances.append(dist)
        temp.append(tree[cur])

        if not to_traverse:
            to_traverse = temp
            dist += 1

            # TODO: Finish computing the traversal distance
            # TODO: Find the distance from u to v


class MyTestCases(unittest.TestCase):
    def test_construct_tree(self):
        n = 5
        node_connections = [1, 2, 2, 4]
        tree = construct_tree(n, node_connections)
        self.assertEqual(len(tree), 5)
        self.assertEqual(len(tree[2]), 2)
        self.assertEqual(len(tree[5]), 0)

    def test_gravity_tree(self):
        n = 5
        node_connections = [1, 2, 2, 4]
        tree = construct_tree(n, node_connections)
        u, v = 2, 1
        self.assertEqual(gravity_tree(tree, u, v), 7)
        u, v = 1, 4
        self.assertEqual(gravity_tree(tree, u, v), 13)
