FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'


def read_input(file_name: str) -> tuple[int, int, int, int]:
    with open(file_name) as file:
        _, _, x, y = file.readline().strip().split()
        x_beg, x_end = x[2:-1].split('..')
        y_beg, y_end = y[2:].split('..')
        return int(x_beg), int(x_end), int(y_beg), int(y_end)
