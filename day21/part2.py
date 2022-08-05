from functools import lru_cache

from day21 import *
from day21.part1 import POSITIONS

WIN_SCORE = 21
SIDES = 3


class Wins:
    def __init__(self, first_wins: int, second_wins: int):
        self.first_wins = first_wins
        self.second_wins = second_wins

    def __add__(self, other):
        self.first_wins += other.first_wins
        self.second_wins += other.second_wins

        return self


@lru_cache(maxsize=None)
def calculate(first_score: int, second_score: int, first_pos: int, second_pos: int, first_turn: bool) -> Wins:
    if first_score >= WIN_SCORE:
        return Wins(1, 0)

    if second_score >= WIN_SCORE:
        return Wins(0, 1)

    res = Wins(0, 0)

    for i in range(SIDES):
        for j in range(SIDES):
            for k in range(SIDES):
                total = i + j + k + 3
                if first_turn:
                    new_pos = (first_pos - 1 + total) % POSITIONS + 1
                    new_score = first_score + new_pos
                    res += calculate(new_score, second_score, new_pos, second_pos, not first_turn)
                else:
                    new_pos = (second_pos - 1 + total) % POSITIONS + 1
                    new_score = second_score + new_pos
                    res += calculate(first_score, new_score, first_pos, new_pos, not first_turn)

    return res


def solution(file_name: str) -> int:
    first_pos, second_pos = read_input(file_name)

    wins = calculate(0, 0, first_pos, second_pos, True)

    return max(wins.first_wins, wins.second_wins)


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 444356092776315

    print(solution(FILE_NAME))
