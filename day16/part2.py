from day16 import *
from day16.part1 import get_type_id


def count(decoded: str) -> tuple[int or None, int or None]:
    if len(decoded) < 11:
        return None, None

    type_id = get_type_id(decoded)

    sub_packages, next_start = get_subpackages(decoded) if type_id != 4 else (None, None)

    match type_id:
        case 0:
            return sum(sub_packages), next_start
        case 1:
            return multiply(sub_packages), next_start
        case 2:
            return min(sub_packages), next_start
        case 3:
            return max(sub_packages), next_start
        case 4:
            return count_number(decoded)
        case 5:
            return int(sub_packages[0] > sub_packages[1]), next_start
        case 6:
            return int(sub_packages[0] < sub_packages[1]), next_start
        case 7:
            return int(sub_packages[0] == sub_packages[1]), next_start


def count_number(decoded: str) -> tuple[int, int]:
    i = 6
    number = ''
    while decoded[i] != '0':
        number += decoded[i + 1: i + 5]
        i = i + 5
    number += decoded[i + 1: i + 5]
    return int(number, 2), i + 5


def multiply(sub_packages: list[int]) -> int:
    prod = 1
    for s in sub_packages:
        prod *= s
    return prod


def get_subpackages(decoded: str) -> tuple[list[int], int]:
    match decoded[6]:
        case '0':
            return subpackages_for_length_type_id_0(decoded)
        case '1':
            return subpackages_for_length_type_id_1(decoded)


def subpackages_for_length_type_id_0(decoded: str) -> tuple[list[int], int]:
    curr = 22
    total_subpackages_length = get_total_subpackages_length(decoded)
    sub_packages = []
    while True:
        sub, next_start = count(decoded[curr: 22 + total_subpackages_length])
        if sub is None:
            return sub_packages, curr
        curr += next_start
        sub_packages.append(sub)


def subpackages_for_length_type_id_1(decoded: str) -> tuple[list[int], int]:
    sub_packages = []
    curr = 18
    for _ in range(get_subpackages_count(decoded)):
        sub, next_start = count(decoded[curr:])
        curr += next_start
        sub_packages.append(sub)
    return sub_packages, curr


def get_subpackages_count(decoded: str) -> int:
    return int(decoded[7:18], 2)


def get_total_subpackages_length(decoded: str) -> int:
    return int(decoded[7:22], 2)


def solution(file_name: str) -> int:
    return count(read_input(file_name))[0]


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME_PART_2_01) == 3
    assert solution(TEST_FILE_NAME_PART_2_02) == 54
    assert solution(TEST_FILE_NAME_PART_2_03) == 7
    assert solution(TEST_FILE_NAME_PART_2_04) == 9
    assert solution(TEST_FILE_NAME_PART_2_05) == 1
    assert solution(TEST_FILE_NAME_PART_2_06) == 0
    assert solution(TEST_FILE_NAME_PART_2_07) == 0
    assert solution(TEST_FILE_NAME_PART_2_08) == 1

    print(solution(FILE_NAME))
