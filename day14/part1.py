from collections import defaultdict

from day14 import *


def solution(file_name: str, number: int) -> int:
    start, mapping = read_input(file_name)
    start_dict = defaultdict(int)
    for i in range(len(start) - 1):
        start_dict[start[i: i + 2]] += 1

    for i in range(number):
        curr_dict = defaultdict(int)
        for pair in start_dict:
            if pair in mapping:
                curr_dict[pair[0] + mapping[pair]] += start_dict[pair]
                curr_dict[mapping[pair] + pair[1]] += start_dict[pair]
            else:
                curr_dict[pair] += 1
        start_dict = curr_dict.copy()
    count_dict = count_letters(start, start_dict)
    return most_common(count_dict) - least_common(count_dict)


def count_letters(start: str, pairs_count) -> dict[str, int]:
    count_dict = defaultdict(int)
    for pair in pairs_count:
        count_dict[pair[0]] += pairs_count[pair]
        count_dict[pair[1]] += pairs_count[pair]

    for letter in count_dict:
        count_dict[letter] //= 2

    count_dict[start[0]] += 1
    count_dict[start[-1]] += 1
    return count_dict


def most_common(count_dict: dict[str, int]) -> int:
    return max(count_dict.values())


def least_common(count_dict: dict[str, int]) -> int:
    return min(count_dict.values())


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME, 10) == 1588

    print(solution(FILE_NAME, 10))
