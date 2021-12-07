from day07 import *


def solution(file_name: str) -> int:
    numbers = read_input(file_name)
    minimum = INFINITY
    for i in range(COUNTER):
        value = 0
        for number in numbers:
            value += abs(number - i)
        minimum = min(minimum, value)
    return minimum


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 37

    print(solution(FILE_NAME))
