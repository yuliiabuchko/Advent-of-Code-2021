from day07 import *


def sum_all(n: int) -> int:
    return n * (n + 1) // 2


def solution(file_name: str) -> int:
    numbers = read_input(file_name)
    minimum = INFINITY
    for i in range(COUNTER):
        value = 0
        for number in numbers:
            value += sum_all(abs(number - i))
        minimum = min(minimum, value)
    return minimum


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 168

    print(solution(FILE_NAME))
