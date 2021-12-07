FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'

INFINITY: float = float("inf")
COUNTER: int = 100


def read_input(file_name: str) -> list[int]:
    with open(file_name) as file:
        return list(map(int, file.readline().split(',')))
