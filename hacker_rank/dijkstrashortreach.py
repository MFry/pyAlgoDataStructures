"""

 Ref: https://www.hackerrank.com/challenges/dijkstrashortreach
 Python input ref: https://dmoj.ca/tips/
"""
import unittest
from heapq import *


def dijkstras(graph, start_node):
    shortest_paths = [float('inf') for _ in range(len(graph) + 1)]
    unvisited = set([i for i in range(len(graph) + 1)])
    shortest_paths[start_node] = 0
    to_visit = []
    heappush(to_visit, (0, start_node))
    while True:
        # partial priority queue implementation
        if not to_visit:
            break
        cur_node = heappop(to_visit)
        # remove the weight
        cur_node = cur_node[1]
        if cur_node in unvisited:
            unvisited.remove(cur_node)
        else:
            continue

        nodes_to_visit = graph[cur_node]
        for node, cost in nodes_to_visit.items():
            current_distance_cost = shortest_paths[cur_node] + cost
            if shortest_paths[node] > current_distance_cost:
                shortest_paths[node] = current_distance_cost
                if node in unvisited:
                    heappush(to_visit, (current_distance_cost, node))

    output = ''
    for i in range(1, len(shortest_paths)):
        if shortest_paths[i] >= float('inf'):
            output += '-1 '
        elif i == start_node:
            continue
        else:
            output += str(shortest_paths[i])
            output += ' '
    return output[:-1]


class MyTestCases(unittest.TestCase):
    def test_dijkstras(self):
        graph = {1: [(2, 24), (4, 20), (3, 4), (3, 3)],
                 2: [(1, 24)],
                 3: [(1, 4), (1, 3), (4, 12)],
                 4: [(3, 12)]}
        start_node = 1
        # print(dijkstras(graph, start_node))
        with open('./test_cases/dijkstras_test_case_1') as f_in, open('./test_cases/dijkstras_output_1') as f_out:
            queries = int(f_in.readline())
            for _ in range(queries):
                nodes, edge_count = [int(i) for i in f_in.readline().split()]
                graph = {}
                for i in range(nodes):
                    graph[i + 1] = {}
                for _ in range(edge_count):
                    node1, node2, weight = [int(i) for i in f_in.readline().split()]
                    connections = [(node1, node2, weight), (node2, node1, weight)]
                    for (key, n2, w) in connections:
                        if n2 in graph[key]:
                            graph[key][n2] = w if graph[key][n2] > w else graph[key][n2]
                        else:
                            graph[key][n2] = w
                start_node = int(f_in.readline())
                self.maxDiff = None
                self.assertEqual(dijkstras(graph, start_node), f_out.readline().strip('\n'))
        import timeit
        start = timeit.default_timer()
        with open('./test_cases/dijkstras_test_case_2') as f_in, open('./test_cases/dijkstras_output_2') as f_out:
            queries = int(f_in.readline())
            for _ in range(queries):
                nodes, edge_count = [int(i) for i in f_in.readline().split()]
                graph = {}
                for i in range(nodes):
                    graph[i + 1] = {}
                for _ in range(edge_count):
                    node1, node2, weight = [int(i) for i in f_in.readline().split()]
                    connections = [(node1, node2, weight), (node2, node1, weight)]
                    for (key, n2, w) in connections:
                        if n2 in graph[key]:
                            graph[key][n2] = w if graph[key][n2] > w else graph[key][n2]
                        else:
                            graph[key][n2] = w
                start_node = int(f_in.readline())
                end = timeit.default_timer()
                print(end - start)
                start = timeit.default_timer()
                self.assertEqual(dijkstras(graph, start_node), f_out.readline().strip('\n'))
                end = timeit.default_timer()
                print(end - start)
