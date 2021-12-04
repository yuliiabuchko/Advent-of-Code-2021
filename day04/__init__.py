from typing import Optional

FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'

BOARD_SIZE: int = 5


class Board:
    def __init__(self, board: list[list[int]]):
        self._board: list[list[Optional[int]]] = board

    def __str__(self):
        return str(self._board)

    def cross_out(self, number: int) -> bool:
        crossed = False
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self._board[i][j] == number:
                    self._board[i][j] = None
                    crossed = True
        return crossed

    def is_winner(self) -> bool:
        for i in range(BOARD_SIZE):
            if self._is_row_crossed_out(i) or self._is_column_crossed_out(i):
                return True
        return False

    def _is_row_crossed_out(self, row_index: int) -> bool:
        for j in range(BOARD_SIZE):
            if self._board[row_index][j] is not None:
                return False
        return True

    def _is_column_crossed_out(self, column_index: int) -> bool:
        for i in range(BOARD_SIZE):
            if self._board[i][column_index] is not None:
                return False
        return True

    def sum_not_crossed(self) -> int:
        return sum(sum(number for number in line if number is not None) for line in self._board)


def read_input(file_name: str) -> tuple[list[int], list[Board]]:
    with open(file_name) as file:
        numbers = list(map(int, file.readline().split(',')))
        boards = []
        curr_board = []
        for i, line in enumerate(file.readlines()):
            if i % (BOARD_SIZE + 1) == 0:
                continue  # empty line
            curr_board.append(list(map(int, line.split())))
            if i % (BOARD_SIZE + 1) == BOARD_SIZE:
                boards.append(Board(curr_board))
                curr_board = []

        return numbers, boards
