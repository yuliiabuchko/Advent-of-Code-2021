from day22 import *

MIN = -50
MAX = 50


class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


def solution(file_name: str) -> int:
    lines = read_input(file_name)

    cubes = set()
    for line in lines:
        for x in range(max(MIN, line.x_start), min(line.x_end, MAX) + 1):
            for y in range(max(MIN, line.y_start), min(line.y_end, MAX) + 1):
                for z in range(max(MIN, line.z_start), min(line.z_end, MAX) + 1):
                    if line.is_on:
                        cubes.add(Cube(x, y, z))
                    else:
                        if Cube(x, y, z) in cubes:
                            cubes.remove(Cube(x, y, z))
    return len(cubes)


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME_SMALL) == 39
    assert solution(TEST_FILE_NAME_LARGE) == 590784
    assert solution(TEST_FILE_NAME_LARGEST) == 474140

    print(solution(FILE_NAME))
