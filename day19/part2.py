from day19 import *
from day19.part1 import normalize_all


def manhattan_distance(first: Probe, second: Probe) -> int:
    return abs(first.x - second.x) + abs(first.y - second.y) + abs(first.z - second.z)


def solution(file_name: str) -> int:
    scanners = read_input(file_name)
    normalize_all(scanners)

    max_manhattan = 0
    for i in range(len(scanners)):
        for j in range(i + 1, len(scanners)):
            max_manhattan = max(max_manhattan, manhattan_distance(scanners[i].distance, scanners[j].distance))

    return max_manhattan


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 3621

    print(solution(FILE_NAME))
