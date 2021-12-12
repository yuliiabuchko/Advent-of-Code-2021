from day09 import *

MAX_POOL_COUNT = 3


def count_pool(lava_pool: list[list[int]], i: int, j: int) -> int:
    if not (0 <= i < len(lava_pool)) or not (0 <= j < len(lava_pool[0])):
        return 0
    if lava_pool[i][j] == 9:
        return 0

    count = 1
    lava_pool[i][j] = 9
    count += count_pool(lava_pool, i - 1, j)
    count += count_pool(lava_pool, i, j - 1)
    count += count_pool(lava_pool, i, j + 1)
    count += count_pool(lava_pool, i + 1, j)
    return count


def get_pools_sizes(lava_map: list[list[int]]) -> list[int]:
    pools_size = []
    for i in range(len(lava_map)):
        for j in range(len(lava_map[0])):
            res = count_pool(lava_map, i, j)
            if res != 0:
                pools_size.append(res)
    return pools_size


def solution(file_name: str) -> int:
    lava_map = read_input(file_name)
    pools_sizes = get_pools_sizes(lava_map)
    res = 1
    for i, max_size in enumerate(sorted(pools_sizes, reverse=True)):
        if i == MAX_POOL_COUNT:
            break
        res *= max_size
    return res


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 1134

    print(solution(FILE_NAME))
