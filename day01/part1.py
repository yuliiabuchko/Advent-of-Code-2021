import day01


def solution(file_name):
    lines = day01.read_lines(file_name)
    counter = 0
    for i in range(1, len(lines)):
        if lines[i] > lines[i - 1]:
            counter += 1
    return counter


if __name__ == '__main__':
    assert solution(day01.TEST_FILE_NAME) == 7

    print(solution(day01.FILE_NAME))
