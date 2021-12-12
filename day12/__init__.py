FILE_NAME: str = 'input.txt'
TEST_FIRST_FILE_NAME: str = 'test_first_input.txt'
TEST_SECOND_FILE_NAME: str = 'test_second_input.txt'
TEST_THIRD_FILE_NAME: str = 'test_third_input.txt'


class Node:
    def __init__(self, cave_name: str):
        self.cave_name = cave_name
        self.visited = False

    def is_small(self) -> bool:
        return self.cave_name.islower() and self.cave_name != Graph.start.cave_name \
               and self.cave_name != Graph.end.cave_name

    def is_visited(self) -> bool:
        return self.visited and self.is_small()

    def __hash__(self):
        return hash(self.cave_name)

    def __eq__(self, other):
        return self.cave_name == other.cave_name


class Graph:
    start = Node('start')
    end = Node('end')

    def __init__(self):
        self.connections: dict[Node, list[Node]] = {}

    def add_connection(self, node_from: Node, node_to: Node):
        if node_to.cave_name == self.start.cave_name or node_from.cave_name == self.end.cave_name:
            return

        if node_from not in self.connections:
            self.connections[node_from] = []
        self.connections[node_from].append(node_to)

    def reset_visited(self):
        for node in self.connections.keys():
            node.visited = False


def read_input(file_name: str) -> Graph:
    graph = Graph()
    name_node = {}
    with open(file_name) as file:
        for line in file.readlines():
            from_cave, to_cave = line.strip().split('-')
            if from_cave not in name_node:
                name_node[from_cave] = Node(from_cave)
            if to_cave not in name_node:
                name_node[to_cave] = Node(to_cave)
            graph.add_connection(name_node[from_cave], name_node[to_cave])
            graph.add_connection(name_node[to_cave], name_node[from_cave])
    return graph
