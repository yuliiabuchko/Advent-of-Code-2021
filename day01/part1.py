from day01 import *


def solution(file_name: str) -> int:
    lines = read_input(file_name)
    counter = 0
    for i in range(1, len(lines)):
        if lines[i] > lines[i - 1]:
            counter += 1
    return counter


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 7

    print(solution(FILE_NAME))
