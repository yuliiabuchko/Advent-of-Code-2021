from day15 import *
from day15.part1 import solve


def increase(levels: list[list[int]], count: int) -> list[list[int]]:
    curr = [level.copy() for level in levels.copy()]
    for i in range(len(levels)):
        for j in range(len(levels[0])):
            curr[i][j] = curr[i][j] + count
            if curr[i][j] > 9:
                curr[i][j] -= 9
    return curr


def bigger_map(levels: list[list[int]]) -> list[list[int]]:
    res = [[] for _ in range(len(levels) * 5)]
    for k in range(5):
        increased = increase(levels, k)
        for start in range(k + 1):
            for i in range(len(levels)):
                res[start * len(levels) + i] += increased[i]
    for k in range(5, 9):
        increased = increase(levels, k)
        for start in range(k - 4, 5):
            for i in range(len(levels)):
                res[start * len(levels) + i] += increased[i]
    return res


def solution(file_name: str) -> int:
    return solve(bigger_map(read_input(file_name)))


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 315

    print(solution(FILE_NAME))
