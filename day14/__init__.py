FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'


def read_input(file_name: str) -> tuple[str, dict[str, str]]:
    with open(file_name) as file:
        start = file.readline().strip()
        file.readline()
        mapping = {}
        for line in file.readlines():
            sequence, letter = line.strip().split(" -> ")
            mapping[sequence] = letter
        return start, mapping
