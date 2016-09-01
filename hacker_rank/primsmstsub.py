"""

Given a graph which consists of several edges connecting the  nodes in it.
It is required to find a subgraph of the given graph with the following properties:

The subgraph contains all the nodes present in the original graph.
The subgraph is of minimum overall weight (sum of all edges) among all such subgraphs.
It is also required that there is exactly one, exclusive path between any two nodes of the subgraph.
One specific node  is fixed as the starting point of finding the subgraph.
Find the total weight of such a subgraph (sum of all edges in the subgraph)

Input Format

First line has two integers
    N, denoting the number of nodes in the graph and
    M, denoting the number of edges in the graph.

The next M lines
    each consist of three space separated integers x y r, where
      x and y denote the two nodes between which the undirected edge exists,
      r denotes the length of edge between the corresponding nodes.

The last line has an integer S, denoting the starting node.


NOTE: If there are edges between the same pair of nodes with different weights,
        they are to be considered as is, like multiple edges.

    Ref: https://www.hackerrank.com/challenges/primsmstsub
"""
from heapq import *
import unittest
import sys


def prims_mst(graph, start_node):
    visited = set()
    to_visit = []
    heappush(to_visit, (0, start_node))
    min_tree_value = 0
    while True:
        current_node = None
        while to_visit:
            current_node = heappop(to_visit)
            if current_node[1] not in visited:
                min_tree_value += current_node[0]
                current_node = current_node[1]
                visited.add(current_node)
                break
            else:
                current_node = None
        if not current_node:
            break

        edges = graph[current_node] if graph[current_node] else []

        for path in edges:
            if path[1] not in visited:
                heappush(to_visit, path)

    return min_tree_value


class MyTestCases(unittest.TestCase):
    def test_primps_mst(self):
        graph = {
            1: [(3, 2), (4, 3)],
            2: [(5, 3), (3, 1), (6, 4), (2, 5)],
            3: [(7, 5), (5, 2), (4, 1)],
            4: [(6, 2)],
            5: [(2, 2), (7, 3)]
        }

        self.assertEqual(prims_mst(graph, 1), 15)


if __name__ == '__main__':
    n, m = [int(i) for i in sys.stdin.readline().split()]
    graph = {}
    for i in range(n + 1):
        graph[i] = []
    for i in range(m):
        node_1, node_2, weight = [int(j) for j in sys.stdin.readline().split()]
        graph[node_1].append((weight, node_2))
        graph[node_2].append((weight, node_1))
    start_node = int(sys.stdin.readline())
    print(prims_mst(graph, start_node))
