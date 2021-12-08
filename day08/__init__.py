from enum import Enum

FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'
TEST_SMALL_FILE_NAME: str = 'test_small_input.txt'


class Number(Enum):
    ZERO = {'a', 'b', 'c', 'e', 'f', 'g'}
    ONE = {'c', 'f'}
    TWO = {'a', 'c', 'd', 'e', 'g'}
    THREE = {'a', 'c', 'd', 'f', 'g'}
    FOUR = {'b', 'c', 'd', 'f'}
    FIVE = {'a', 'b', 'd', 'f', 'g'}
    SIX = {'a', 'b', 'd', 'e', 'f', 'g'}
    SEVEN = {'a', 'c', 'f'}
    EIGHT = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    NINE = {'a', 'b', 'c', 'd', 'f', 'g'}

    def __int__(self):
        for i, number in enumerate(self.all_numbers()):
            if self == number:
                return i

    def __len__(self):
        return len(self.value)

    @staticmethod
    def all_numbers() -> list:
        return [Number.ZERO, Number.ONE, Number.TWO, Number.THREE, Number.FOUR, Number.FIVE, Number.SIX,
                Number.SEVEN, Number.EIGHT, Number.NINE]


class Entry:
    def __init__(self, patterns: list[set], output: list[set]):
        self.patterns = patterns
        self.output = output


def read_input(file_name: str) -> list[Entry]:
    with open(file_name) as file:
        res = []
        for line in file.readlines():
            patterns, out = line.strip().split('|')
            entry_patterns = []
            for pattern in patterns.strip().split():
                entry_patterns.append(set(list(pattern)))
            entry_outputs = []
            for output in out.strip().split():
                entry_outputs.append(set(list(output)))
            res.append(Entry(entry_patterns, entry_outputs))
        return res
