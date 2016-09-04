"""

 ref: https://www.hackerrank.com/challenges/kruskalmstrsub
"""
import sys
import unittest


def compare_edges(a, b):
    if a[2] < b[2]:
        return -1
    if a[2] > b[2]:
        return 1
    else:
        a = a[0] + a[1] + a[2]
        b = b[0] + b[1] + b[2]
        if a < b:
            return -1
        else:
            return 1


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'

    class K:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


def kruskal_mst(edges):
    edges.sort(key=cmp_to_key(compare_edges))
    trees = []
    weighted_sum = 0
    for edge in edges:
        edge_weight = edge[2]
        edge = {edge[0], edge[1]}
        max_common_edges = -1
        for tree in trees:
            common_edges = edge.intersection(tree)
            if len(common_edges) > 1:
                max_common_edges = 2
                break
            if len(common_edges) == 1:
                max_common_edges = 1
        if max_common_edges > 1:
            continue
        elif max_common_edges == 1:
            i = 0
            while i < len(trees):
                if edge.intersection(trees[i]):
                    edge = edge.union(trees[i])
                    trees.pop(i)
                else:
                    i += 1
        trees.append(edge)
        weighted_sum += edge_weight

    return weighted_sum


n, m = [int(i) for i in sys.stdin.readline().split()]
edges = []
for i in range(m):
    node_1, node_2, weight = [int(j) for j in sys.stdin.readline().split()]
    edges.append((node_1, node_2, weight))
start_node = int(sys.stdin.readline())
print(kruskal_mst(edges))
