from day11 import *

STEPS = 100


def is_in_table(i: int, j: int) -> bool:
    return 0 <= i < SIZE and 0 <= j < SIZE


def adjacent(i: int, j: int) -> list[tuple[int, int]]:
    res = []
    for (i_, j_) in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1),
                     (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
        if is_in_table(i_, j_):
            res.append((i_, j_))
    return res


def flash(current: list[list[int]], i: int, j: int):
    closest = adjacent(i, j)
    for (i_, j_) in closest:
        if current[i_][j_] == 10:
            continue
        current[i_][j_] += 1
        if current[i_][j_] == 10:
            flash(current, i_, j_)


def count_flash_and_reset(current: list[list[int]]) -> int:
    res = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if current[i][j] == 10:
                current[i][j] = 0
                res += 1
    return res


def next_step(current: list[list[int]]) -> int:
    for i in range(SIZE):
        for j in range(SIZE):
            if current[i][j] == 10:
                continue
            current[i][j] += 1
            if current[i][j] == 10:
                flash(current, i, j)
    return count_flash_and_reset(current)


def solution(file_name: str) -> int:
    initial_energy = read_input(file_name)
    res = 0
    for i in range(STEPS):
        res += next_step(initial_energy)
    return res


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 1656

    print(solution(FILE_NAME))
