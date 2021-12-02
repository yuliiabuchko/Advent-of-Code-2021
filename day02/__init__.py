from enum import Enum

FILE_NAME = 'input.txt'
TEST_FILE_NAME = 'test_input.txt'


class Directions(Enum):
    FORWARD = 'forward'
    DOWN = 'down'
    UP = 'up'


class InputLine:
    def __init__(self, direction, size):
        self.direction = direction
        self.size = size


def read_lines(file_name):
    result = []
    with open(file_name) as file:
        for line in file:
            direction, size = line.split(' ')
            result.append(InputLine(Directions(direction), int(size)))
    return result
