"""
Ref: https://www.hackerrank.com/challenges/bfsshortreach

docs: https://docs.python.org/2/tutorial/datastructures.html
"""
import unittest
from collections import deque


def bfs(graph, start_node):
    """

    :param graph:
    :type graph: dict
    :param start_node:
    :return:
    """
    shortest_paths = [-1] * (len(graph) + 1)
    shortest_paths[start_node] = 0
    to_visit = deque([start_node])
    while to_visit:
        cur_node = to_visit.popleft()
        nodes = graph[cur_node]
        if not nodes:
            continue
        for node in nodes:
            shortest_paths[node] = shortest_paths[cur_node] + 6
            to_visit.append(node)
    output = ''
    for i in range(1, len(shortest_paths)):
        if i == start_node:
            continue
        output += str(shortest_paths[i]) + " "
    return output[:-1]


class MyTestCases(unittest.TestCase):
    graph = {1: [2, 3],
             2: None,
             3: None,
             4: None}
    start_node = 1
    print(bfs(graph, start_node))
