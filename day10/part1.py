from typing import Optional

from day10 import *

SCORE_ILLEGAL = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def get_first_illegal_char(line: list[str]) -> Optional[chr]:
    stack = []
    for c in line:
        if c in CHUNKS_MAPPING:
            stack.append(c)
        else:
            latest_opened = stack.pop()
            if CHUNKS_MAPPING[latest_opened] != c:
                return c


def solution(file_name: str) -> int:
    lines = read_input(file_name)
    score = 0
    for line in lines:
        illegal_char = get_first_illegal_char(line)
        if illegal_char is not None:
            score += SCORE_ILLEGAL[illegal_char]
    return score


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 26397

    print(solution(FILE_NAME))
