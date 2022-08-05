from day21 import *

WIN_SCORE: int = 1000
SIDES: int = 100
POSITIONS: int = 10


def sum_next_three_tosses(i: int) -> int:
    if i <= SIDES - 2:
        return 3 * (i + 1)
    if i == SIDES - 1:
        return 2 * i + 1 + 1
    if i == SIDES:
        return i + 1 + 2


def get_next_roll_start(i: int) -> int:
    return (i + 2) % SIDES + 1


def get_next_position(curr_pos: int, delta: int) -> int:
    return (curr_pos + delta - 1) % POSITIONS + 1


def solution(file_name: str) -> int:
    first_pos, second_pos = read_input(file_name)
    first_score = second_score = 0

    first_turn = True

    i = 1
    tosses = 0
    while first_score < WIN_SCORE and second_score < WIN_SCORE:
        if first_turn:
            first_pos = get_next_position(first_pos, sum_next_three_tosses(i))
            first_score += first_pos
        else:
            second_pos = get_next_position(second_pos, sum_next_three_tosses(i))
            second_score += second_pos
        first_turn = not first_turn
        i = get_next_roll_start(i)
        tosses += 3

    return min(first_score, second_score) * tosses


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 739785

    print(solution(FILE_NAME))
