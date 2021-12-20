from day20 import *


def get_sub_pixels(image: list[list[chr]], i: int, j: int) -> int:
    top = image[i - 1][j - 1: j + 2]
    middle = image[i][j - 1: j + 2]
    bottom = image[i + 1][j - 1: j + 2]

    string = ''.join(top + middle + bottom)
    transformed = string.replace('.', '0').replace('#', '1')
    return int(transformed, 2)


def update(image: list[list[chr]], algorithm: list[chr]) -> list[list[chr]]:
    res = [c.copy() for c in image]
    for i in range(3, len(image) - 3):
        for j in range(3, len(image[0]) - 3):
            new = get_sub_pixels(image, i, j)
            res[i][j] = algorithm[new]
    return res


def solution(file_name: str, count: int) -> int:
    algorithm, image = read_input(file_name)
    for _ in range(count):
        image = update(image, algorithm)

    res = 0
    for i in range(SAFE_DISTANCE, len(image) - SAFE_DISTANCE):
        for j in range(SAFE_DISTANCE, len(image[0]) - SAFE_DISTANCE):
            if image[i][j] == '#':
                res += 1

    return res


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME, 2) == 35

    print(solution(FILE_NAME, 2))
