from day11 import *

STEPS = 100


def adjacent(i: int, j: int) -> list[tuple[int, int]]:
    res = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
           (i, j - 1), (i, j + 1),
           (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
    if i == 0:
        res.remove((i - 1, j - 1))
        res.remove((i - 1, j))
        res.remove((i - 1, j + 1))
    if i == SIZE - 1:
        res.remove((i + 1, j - 1))
        res.remove((i + 1, j))
        res.remove((i + 1, j + 1))

    if j == 0:
        if (i - 1, j - 1) in res:
            res.remove((i - 1, j - 1))
        if (i, j - 1) in res:
            res.remove((i, j - 1))
        if (i + 1, j - 1) in res:
            res.remove((i + 1, j - 1))
    if j == SIZE - 1:
        if (i - 1, j + 1) in res:
            res.remove((i - 1, j + 1))
        if (i, j + 1) in res:
            res.remove((i, j + 1))
        if (i + 1, j + 1) in res:
            res.remove((i + 1, j + 1))
    return res


def flash(current: list[list[int]], i: int, j: int):
    closest = adjacent(i, j)
    for (i_, j_) in closest:
        if current[i_][j_] == 10:
            continue
        current[i_][j_] += 1
        if current[i_][j_] == 10:
            flash(current, i_, j_)


def set_flash_to_zero(current: list[list[int]]) -> int:
    res = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if current[i][j] >= 10:
                current[i][j] = 0
                res += 1
    return res


def next_step(current: list[list[int]]) -> int:
    for i in range(SIZE):
        for j in range(SIZE):
            current[i][j] += 1
            if current[i][j] == 10:
                flash(current, i, j)
    return set_flash_to_zero(current)


def solution(file_name: str) -> int:
    initial_energy = read_input(file_name)
    res = 0
    for i in range(STEPS):
        res += next_step(initial_energy)
        print(i + 1, res, initial_energy)
    return res


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 1656

    print(solution(FILE_NAME))
