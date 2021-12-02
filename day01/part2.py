import day01


def solution(file_name):
    lines = day01.read_lines(file_name)
    counter = 0
    prev_sum = sum(lines[0:3])
    for i in range(3, len(lines)):
        curr_sum = prev_sum + lines[i] - lines[i - 3]
        if curr_sum > prev_sum:
            counter += 1
        prev_sum = curr_sum
    return counter


if __name__ == '__main__':
    assert solution(day01.TEST_FILE_NAME) == 5

    print(solution(day01.FILE_NAME))
