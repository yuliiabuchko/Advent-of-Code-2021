from day16 import *


def get_version(decoded: str) -> int:
    return int(decoded[:3], 2)


def get_type_id(decoded: str) -> int:
    return int(decoded[3:6], 2)


def count_version(decoded: str) -> int:
    if len(decoded) < 11:
        return 0

    if get_type_id(decoded) != 4:
        return get_version(decoded) + count_version(decoded[22 if decoded[6] == '0' else 18:])

    i = 6
    while decoded[i] != '0':
        i = i + 5
    return get_version(decoded) + count_version(decoded[i + 5:])


def solution(file_name: str) -> int:
    return count_version(read_input(file_name))


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME_PART_1_01) == 6
    assert solution(TEST_FILE_NAME_PART_1_02) == 9
    assert solution(TEST_FILE_NAME_PART_1_03) == 14
    assert solution(TEST_FILE_NAME_PART_1_04) == 16
    assert solution(TEST_FILE_NAME_PART_1_05) == 12
    assert solution(TEST_FILE_NAME_PART_1_06) == 23
    assert solution(TEST_FILE_NAME_PART_1_07) == 31

    print(solution(FILE_NAME))
