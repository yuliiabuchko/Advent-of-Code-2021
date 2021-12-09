from day09 import *


def is_lover(lava_map: list[list[int]], i: int, j: int, compared_i: int, compared_j: int) -> bool:
    if compared_i < 0 or compared_j < 0 or compared_i >= len(lava_map) or compared_j >= len(lava_map[0]):
        return True
    return lava_map[i][j] < lava_map[compared_i][compared_j]


def count_if_lower(lava_map: list[list[int]], i: int, j: int) -> int:
    top = (i - 1, j)
    left = (i, j - 1)
    right = (i, j + 1)
    bottom = (i + 1, j)

    if is_lover(lava_map, i, j, *top) and is_lover(lava_map, i, j, *left) \
            and is_lover(lava_map, i, j, *right) and is_lover(lava_map, i, j, *bottom):
        return lava_map[i][j] + 1
    return 0


def solution(file_name: str) -> int:
    lava_map = read_input(file_name)

    count = 0
    for i in range(len(lava_map)):
        for j in range(len(lava_map[0])):
            count += count_if_lower(lava_map, i, j)
    return count


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 15

    print(solution(FILE_NAME))
