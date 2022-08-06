FILE_NAME: str = 'input.txt'
TEST_FILE_NAME_SMALL: str = 'test_input_small.txt'
TEST_FILE_NAME_LARGE: str = 'test_input_large.txt'
TEST_FILE_NAME_LARGEST: str = 'test_input_largest.txt'


class InputLine:
    def __init__(self, is_on: bool, x_start, x_end, y_start, y_end, z_start, z_end):
        self.is_on = is_on
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        self.z_start = z_start
        self.z_end = z_end


def read_input(file_name: str) -> list[InputLine]:
    res = []
    with open(file_name) as file:
        for line in file.readlines():
            status, coordinates = line.strip().split()
            x_range, y_range, z_range = coordinates.split(",")
            _, x_range = x_range.split("=")
            _, y_range = y_range.split("=")
            _, z_range = z_range.split("=")
            x_start, x_end = map(int, x_range.split(".."))
            y_start, y_end = map(int, y_range.split(".."))
            z_start, z_end = map(int, z_range.split(".."))
            res.append(InputLine(status == "on", x_start, x_end, y_start, y_end, z_start, z_end))
    return res
