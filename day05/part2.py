from day05 import *
from day05.part1 import solution


def filter_input(lines: list[Line]) -> list[Line]:
    res = []
    for line in lines:
        if line.is_horizontal() or line.is_vertical() or line.is_diagonal():
            res.append(line)
    return res


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME, filter_input) == 12

    print(solution(FILE_NAME, filter_input))
