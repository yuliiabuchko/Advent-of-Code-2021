from day02 import *


def solution(file_name: str) -> int:
    lines = read_input(file_name)
    depth = 0
    horizontal_pos = 0
    aim = 0
    for line in lines:
        if line.direction == Directions.FORWARD:
            horizontal_pos += line.size
            depth += aim * line.size
        elif line.direction == Directions.UP:
            aim -= line.size
        elif line.direction == Directions.DOWN:
            aim += line.size
    return depth * horizontal_pos


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 900

    print(solution(FILE_NAME))
