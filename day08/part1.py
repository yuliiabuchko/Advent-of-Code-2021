from day08 import *


def solution(file_name):
    entries = read_input(file_name)

    return sum(int(len(out) in map(len, [Number.ONE, Number.FOUR, Number.SEVEN, Number.EIGHT]))
               for entry in entries for out in entry.output)


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 26

    print(solution(FILE_NAME))
