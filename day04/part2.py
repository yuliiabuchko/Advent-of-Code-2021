from day04 import *


def solution(file_name: str) -> int:
    numbers, boards = read_input(file_name)
    for number in numbers:
        possible_winners = []
        for i, board in enumerate(boards):
            if board.cross_out(number):
                possible_winners.append((i, board))
        indexes_to_remove = []
        for index, board in possible_winners:
            if board.is_winner():
                if len(boards) == 1:
                    return board.sum_not_crossed() * number
                indexes_to_remove.append(index)
        for index in reversed(sorted(indexes_to_remove)):
            boards.pop(index)


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 1924

    print(solution(FILE_NAME))
