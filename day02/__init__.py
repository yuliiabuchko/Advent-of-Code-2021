from enum import Enum

FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'


class Directions(Enum):
    FORWARD: str = 'forward'
    DOWN: str = 'down'
    UP: str = 'up'


class InputLine:
    def __init__(self, direction: Directions, size: int):
        self.direction = direction
        self.size = size


def read_lines(file_name: str) -> list[InputLine]:
    result = []
    with open(file_name) as file:
        for line in file:
            direction, size = line.split(' ')
            result.append(InputLine(Directions(direction), int(size)))
    return result
