from day10 import *

MULTIPLIER = 5
SCORE_INCOMPLETE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def get_incomplete_str(line: list[str]) -> list[chr]:
    stack = []
    for i, c in enumerate(line):
        if c in CHUNKS_MAPPING:
            stack.append(c)
        else:
            latest_opened = stack.pop()
            if CHUNKS_MAPPING[latest_opened] != c:
                return []
    return stack


def solution(file_name: str) -> int:
    lines = read_input(file_name)
    scores = []
    for line in lines:
        incomplete = get_incomplete_str(line)
        if not incomplete:
            continue
        scores.append(count_score(incomplete))
    return sorted(scores)[len(scores) // 2]


def count_score(incomplete: list[chr]) -> int:
    score = 0
    for c in reversed(incomplete):
        score = score * MULTIPLIER + SCORE_INCOMPLETE[CHUNKS_MAPPING[c]]
    return score


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 288957

    print(solution(FILE_NAME))
