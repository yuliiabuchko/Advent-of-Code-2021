from day04 import *


def solution(file_name: str) -> int:
    numbers, boards = read_input(file_name)
    for number in numbers:
        possible_winners = []
        for board in boards:
            if board.cross_out(number):
                possible_winners.append(board)
        for board in possible_winners:
            if board.is_winner():
                return board.sum_not_crossed() * number


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 4512

    print(solution(FILE_NAME))
