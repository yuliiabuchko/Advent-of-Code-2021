FILE_NAME = 'input.txt'
TEST_FILE_NAME = 'test_input.txt'


def read_lines(file_name):
    with open(file_name) as file:
        return list(map(int, file.readlines()))
