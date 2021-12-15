FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'


def read_input(file_name: str) -> list[list[int]]:
    levels = []
    with open(file_name) as file:
        for line in file.readlines():
            levels.append(list(map(int, list(line.strip()))))
    return levels
