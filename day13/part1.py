from day13 import *


def solution(file_name: str) -> int:
    dots, folds = read_input(file_name)
    res = set()
    first_fold = folds[0]
    for dot in dots:
        dot.fold(*first_fold)
        res.add(dot)
    return len(res)


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 17

    print(solution(FILE_NAME))
