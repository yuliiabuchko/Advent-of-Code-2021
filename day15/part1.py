import heapq
import sys

from day15 import *


class Node:
    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j

    def __str__(self):
        return f'({self.i},{self.j})'

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __hash__(self):
        return hash(str(self))

    def __lt__(self, other):
        return str(self) < str(other)


class Graph:
    def __init__(self):
        self.connections: dict[Node, dict[Node, int]] = {}

    def add_connection(self, from_node: Node, to_node: Node, cost: int):
        if from_node not in self.connections:
            self.connections[from_node] = {}
        self.connections[from_node][to_node] = cost


def connect_if_correct(graph: Graph, start: Node, i: int, j: int, levels: list[list[int]]) -> None:
    if 0 <= i < len(levels) and 0 <= j < len(levels[0]):
        graph.add_connection(start, Node(i, j), levels[i][j])


def solve(levels: list[list[int]]) -> int:
    graph = create_graph(levels)

    source = Node(0, 0)
    distances_from_source: dict[Node, int] = {source: 0}
    for vertex in graph.connections:
        if vertex != source:
            distances_from_source[vertex] = sys.maxsize

    pq = [(0, source)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances_from_source[current_vertex]:
            continue

        for vertex in graph.connections[current_vertex]:
            alt_distance = distances_from_source[current_vertex] + graph.connections[current_vertex][vertex]
            if alt_distance < distances_from_source[vertex]:
                distances_from_source[vertex] = alt_distance
                heapq.heappush(pq, (alt_distance, vertex))

    return distances_from_source[Node(len(levels) - 1, len(levels) - 1)]


def create_graph(levels: list[list[int]]) -> Graph:
    graph = Graph()
    for i in range(len(levels)):
        for j in range(len(levels[0])):
            curr = Node(i, j)
            connect_if_correct(graph, curr, i + 1, j, levels)
            connect_if_correct(graph, curr, i - 1, j, levels)
            connect_if_correct(graph, curr, i, j + 1, levels)
            connect_if_correct(graph, curr, i, j - 1, levels)
    return graph


def solution(file_name: str) -> int:
    return solve(read_input(file_name))


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 40

    print(solution(FILE_NAME))
