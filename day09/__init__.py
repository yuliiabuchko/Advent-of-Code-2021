FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'


def read_input(file_name: str) -> list[list[int]]:
    with open(file_name) as file:
        lines = list(map(str.strip, file.readlines()))
        res = []
        for line in lines:
            res.append(list(map(int, list(line))))
        return res
