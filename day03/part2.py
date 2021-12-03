from typing import Callable

from day03 import *


def common_filter(bits: list[str], index: int, function: Callable[[int], str]) -> list[str]:
    if index == len(bits[0]) or len(bits) <= 1:
        return bits
    pos_count = count_pos_bits(bits, index)
    return common_filter(list(filter(lambda line: line[index] == function(pos_count), bits)), index + 1, function)


def most_common_bit(pos_count: int):
    if pos_count >= 0:
        return '1'
    return '0'


def least_common_bit(pos_count: int):
    if pos_count >= 0:
        return '0'
    return '1'


def count_pos_bits(bits: list[str], index: int) -> int:
    pos_count = 0
    for line in bits:
        if line[index] == '1':
            pos_count += 1
        elif line[index] == '0':
            pos_count -= 1
    return pos_count


def solution(file_name: str) -> int:
    lines = read_lines(file_name)
    oxygen_generator_rating = int(str(common_filter(lines, 0, most_common_bit)[0]), base=2)
    scrubber_rating = int(str(common_filter(lines, 0, least_common_bit)[0]), base=2)
    return oxygen_generator_rating * scrubber_rating


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 230

    print(solution(FILE_NAME))
