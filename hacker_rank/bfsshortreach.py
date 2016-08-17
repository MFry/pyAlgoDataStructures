"""
    Difficulty: **
    Code: ****

Given a graph consisting N nodes (labelled 1 to N) where a specific given node S represents the starting position
  S and an edge between two nodes is of a given length, which may or may not be equal to other lengths in the graph.

It is required to calculate the shortest distance from the start position (Node S)
 to all of the other nodes in the graph.

Note: If a node is unreachable , the distance is assumed as -1.

Ref: https://www.hackerrank.com/challenges/bfsshortreach

docs: https://docs.python.org/3/tutorial/datastructures.html
      https://docs.python.org/3/library/collections.html#collections.deque
"""
import unittest
from heapq import *


def bfs(graph, start_node):
    """

    :param graph:
    :type graph: dict
    :param start_node:
    :return:
    """
    shortest_paths = [float('inf')] * (len(graph) + 1)
    unvisited = set([i for i in range(len(graph) + 1)])
    shortest_paths[start_node] = 0
    to_visit = []
    heappush(to_visit, (0, start_node))
    while True:
        # this is essentially a partial priority queue
        # check if heap is empty and we are done
        if not to_visit:
            break
        cur_node = heappop(to_visit)

        if cur_node[1] in unvisited:
            unvisited.remove(cur_node[1])
        else:
            continue
        if cur_node is None:
            break
        # end partial priority queue

        # cur_node = (best_distance, node)
        cur_node = cur_node[1]
        nodes = graph[cur_node] if graph[cur_node] else []
        # Calculate all the distances from the current node
        for node in nodes:
            distance_found = shortest_paths[cur_node] + 6
            if shortest_paths[node] > distance_found:
                shortest_paths[node] = distance_found

            heappush(to_visit, (distance_found, node))

    output = ''
    for i in range(1, len(shortest_paths)):
        if i == start_node:
            continue
        elif shortest_paths[i] == float('inf'):
            shortest_paths[i] = -1
        output += str(shortest_paths[i]) + " "
    return output[:-1]


class MyTestCases(unittest.TestCase):
    def test_bfs(self):
        # sample test cases with
        graph = {1: [2, 3],
                 2: None,
                 3: None,
                 4: None}
        start_node = 1
        self.assertEqual(bfs(graph, start_node), '6 6 -1')
        graph = {1: None,
                 2: [3],
                 3: None}
        start_node = 2
        self.assertEqual(bfs(graph, start_node), '-1 6')
        with open('./test_cases/bfs_test_case_1') as f:
            queries = int(f.readline().strip())
            for _ in range(queries):
                node_count, edge_count = [int(i) for i in f.readline().split(' ')]
                graph = {}
                for i in range(node_count):
                    graph[i + 1] = None
                for i in range(edge_count):
                    node1, node2 = [int(i) for i in f.readline().split(' ')]
                    connections = [(node1, node2), (node2, node1)]
                    for (key, connected_to) in connections:
                        if graph[key]:
                            graph[key].append(connected_to)
                        else:
                            graph[key] = [connected_to]
                start_node = int(f.readline().strip())
                print(bfs(graph, start_node))


if __name__ == '__main__':
    queries = int(input().strip())
    for _ in range(queries):
        node_count, edge_count = [int(i) for i in input().split(' ')]
        graph = {}
        for i in range(node_count):
            graph[i + 1] = None
        for i in range(edge_count):
            key, connected_to = [int(i) for i in input().split(' ')]
            if graph[key]:
                graph[key].append(connected_to)
            else:
                graph[key] = [connected_to]
        start_node = int(input().strip())
        bfs(graph, start_node)
