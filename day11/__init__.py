FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'

SIZE = 10


def read_input(file_name: str) -> list[list[int]]:
    with open(file_name) as file:
        res = []
        for line in file.readlines():
            res.append(list(map(int, list(line.strip()))))
        return res
