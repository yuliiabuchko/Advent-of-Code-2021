from collections import defaultdict

from day12 import *
from day12.part1 import solution


def can_visit(curr_path: list[Node], curr_node: Node) -> bool:
    count = defaultdict(int)
    for node in curr_path:
        if node.is_small():
            count[node.cave_name] += 1
    if curr_node.is_small():
        count[curr_node.cave_name] += 1
    v = list(count.values())
    return v.count(2) <= 1 and not v.count(3)


if __name__ == '__main__':
    assert solution(TEST_FIRST_FILE_NAME, can_visit) == 36
    assert solution(TEST_SECOND_FILE_NAME, can_visit) == 103
    assert solution(TEST_THIRD_FILE_NAME, can_visit) == 3509

    print(solution(FILE_NAME, can_visit))
