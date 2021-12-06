from day06 import *

TIME_TO_CREATE_LANTERNFISH = 6
TIME_TO_CREATE_FIRST_LANTERNFISH = 8


def count_lanternfishes(number_of_days: int) -> dict[int, int]:
    lanternfishes = {}
    for i in range(TIME_TO_CREATE_LANTERNFISH - TIME_TO_CREATE_FIRST_LANTERNFISH,
                   number_of_days + TIME_TO_CREATE_FIRST_LANTERNFISH):
        if i < 0:
            lanternfishes[i] = 0
        else:
            j = i
            count = 1
            first_child = True
            while j > TIME_TO_CREATE_LANTERNFISH:
                if first_child:
                    j -= TIME_TO_CREATE_FIRST_LANTERNFISH + 1
                    first_child = False
                else:
                    j -= TIME_TO_CREATE_LANTERNFISH + 1
                count += lanternfishes[j]
            lanternfishes[i] = count
    return lanternfishes


def solution(file_name: str, number_of_days: int) -> int:
    numbers = read_input(file_name)
    lanternfishes = count_lanternfishes(number_of_days)
    return sum(lanternfishes[number_of_days + TIME_TO_CREATE_FIRST_LANTERNFISH - number] for number in numbers)


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME, 18) == 26
    assert solution(TEST_FILE_NAME, 80) == 5934

    print(solution(FILE_NAME, 80))
