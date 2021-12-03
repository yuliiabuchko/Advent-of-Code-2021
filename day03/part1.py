from day03 import *


def parse_count_to_bits(bits_count: list[int]) -> str:
    res = ''
    for number in bits_count:
        if number > 0:
            res += '1'
        else:
            res += '0'
    return res


def flip_count(bits: str) -> str:
    res = ''
    for bit in bits:
        if bit == '0':
            res += '1'
        elif bit == '1':
            res += '0'
    return res


def solution(file_name: str) -> int:
    lines = read_lines(file_name)
    positives_count = [0 for _ in range(len(lines[0]))]
    for line in lines:
        for i in range(len(line)):
            if line[i] == '1':
                positives_count[i] += 1
            elif line[i] == '0':
                positives_count[i] -= 1
    gamma_rate_bits = parse_count_to_bits(positives_count)
    epsilon_rate_bits = flip_count(gamma_rate_bits)
    return int(gamma_rate_bits, base=2) * int(epsilon_rate_bits, base=2)


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 198

    print(solution(FILE_NAME))
