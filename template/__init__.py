FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'


def read_lines(file_name: str) -> list[str]:
    with open(file_name) as file:
        return list(map(str.strip, file.readlines()))
