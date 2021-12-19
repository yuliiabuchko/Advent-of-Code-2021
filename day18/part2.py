from day18 import *
from day18.part1 import add, count_magnitude


def solution(file_name: str) -> int:
    numbers = read_input(file_name)
    maximum = 0
    for first in numbers:
        for second in numbers:
            if first != second:
                maximum = max(maximum, count_magnitude(add(first, second)))
    return maximum


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME_7) == 3993

    print(solution(FILE_NAME))
