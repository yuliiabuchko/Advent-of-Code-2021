from typing import Callable

from day12 import *


def can_visit(_: list[Node], node: Node) -> bool:
    return not node.is_visited()


def get_paths(start_node: Node, graph: Graph, curr_path: list[Node], all_paths: list[list[Node]],
              can_visit_function: Callable[[list[Node], Node], bool]) -> list[list[Node]]:
    for node in graph.connections[start_node]:
        if node == graph.end:
            curr_path.append(graph.end)
            all_paths.append(curr_path.copy())
            curr_path.pop()
            continue

        if not can_visit_function(curr_path, node):
            continue
        curr_path.append(node)
        node.visited = True
        get_paths(node, graph, curr_path, all_paths, can_visit_function)
        node.visited = False
        curr_path.pop()
    return all_paths


def solution(file_name: str, visit_fun: Callable[[list[Node], Node], bool]) -> int:
    graph = read_input(file_name)
    curr_path = [graph.start]
    graph.start.visited = True
    return len(get_paths(graph.start, graph, curr_path, [], visit_fun))


if __name__ == '__main__':
    assert solution(TEST_FIRST_FILE_NAME, can_visit) == 10
    assert solution(TEST_SECOND_FILE_NAME, can_visit) == 19
    assert solution(TEST_THIRD_FILE_NAME, can_visit) == 226

    print(solution(FILE_NAME, can_visit))
