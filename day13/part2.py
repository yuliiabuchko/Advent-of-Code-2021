from day13 import *


def solution(file_name: str) -> None:
    dots, folds = read_input(file_name)
    res = set()
    for fold in folds:
        for dot in dots:
            dot.fold(*fold)
            res.add(dot)

    image = [['.' for _ in range(40)] for _ in range(6)]
    for dot in res:
        image[dot.y][dot.x] = '#'
    for line in image:
        print(' '.join(line))
    print()


if __name__ == '__main__':
    solution(TEST_FILE_NAME)

    solution(FILE_NAME)
