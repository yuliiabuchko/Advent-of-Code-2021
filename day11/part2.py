from day11 import *
from day11.part1 import next_step


def solution(file_name: str) -> int:
    initial_energy = read_input(file_name)
    i = 0
    while next_step(initial_energy) != SIZE * SIZE:
        i += 1
    return i + 1


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 195

    print(solution(FILE_NAME))
