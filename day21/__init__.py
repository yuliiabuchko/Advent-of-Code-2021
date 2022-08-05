FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'


def read_input(file_name: str) -> tuple[int, int]:
    with open(file_name) as file:
        first = int(file.readline().split()[4])
        second = int(file.readline().split()[4])
        return first, second
