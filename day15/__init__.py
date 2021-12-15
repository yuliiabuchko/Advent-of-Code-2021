FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'


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


def read_input(file_name: str) -> list[list[int]]:
    levels = []
    with open(file_name) as file:
        for line in file.readlines():
            levels.append(list(map(int, list(line.strip()))))
    return levels
