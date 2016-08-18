"""

 Ref: https://www.hackerrank.com/challenges/dijkstrashortreach

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
        if cur_node[1] in unvisited:
            unvisited.remove(cur_node[1])
        else:
            continue

        # remove the weight
        cur_node = cur_node[1]

        nodes_to_visit = graph[cur_node] if graph[cur_node] else []
        for (node, cost) in nodes_to_visit:
            current_distance_cost = shortest_paths[cur_node] + cost
            if shortest_paths[node] > current_distance_cost:
                shortest_paths[node] = current_distance_cost
                heappush(to_visit, (current_distance_cost, node))

    output = ''
    for i in range(1, len(shortest_paths)):
        if i == float('inf'):
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
        print(dijkstras(graph, start_node))


if __name__ == '__main__':
    queries = int(input().strip())
    for _ in range(queries):
        node_count, edge_count = [int(i) for i in input().split(' ')]
        graph = {}
        for i in range(node_count):
            graph[i + 1] = None
        for i in range(edge_count):
            node1, node2, weight = [int(i) for i in input().split(' ')]
            connections = [(node1, node2, weight), (node2, node1, weight)]
            # TODO: Take into account duplicate edges
            for (key, connected_to, weight) in connections:
                if graph[key]:
                    graph[key].append((connected_to, weight))
                else:
                    graph[key] = [(connected_to, weight)]
        start_node = int(input().strip())
        print(dijkstras(graph, start_node))
