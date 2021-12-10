FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'

CHUNKS_MAPPING = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def read_input(file_name: str) -> list[list[str]]:
    with open(file_name) as file:
        return list(map(list, (map(str.strip, file.readlines()))))
