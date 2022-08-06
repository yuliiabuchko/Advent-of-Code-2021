from day18 import *


def add(left: Number, right: Number) -> Number:
    return reduce(Number(left, right))


def reduce(number: Number) -> Number:
    if can_explode(number):
        return reduce(explode(number))
    if can_split(number):
        return reduce(split(number))
    return number


def can_explode(number: Number) -> bool:
    def can_explode_helper(num: Number, curr_height: int) -> bool:
        if curr_height > 4:
            return True
        if isinstance(num, int):
            return False
        return can_explode_helper(num.left, curr_height + 1) or can_explode_helper(num.right, curr_height + 1)

    return can_explode_helper(number, 0)


def can_split(number: Number) -> bool:
    if isinstance(number, int):
        if number >= 10:
            return True
        return False
    return can_split(number.left) or can_split(number.right)


def split(number: Number) -> Number:
    def number_to_split(num: Number) -> int or None:
        if isinstance(num, int):
            if num >= 10:
                return num
            return None
        left_number_to_split = number_to_split(num.left)
        return left_number_to_split if left_number_to_split else number_to_split(num.right)

    to_split = number_to_split(number)
    left_replacement = to_split // 2
    right_replacement = left_replacement + (1 if to_split % 2 == 1 else 0)

    left, right = str(number).split(str(to_split), 1)
    return string_number_to_number(left + str(Number(left_replacement, right_replacement)) + right)


def explode(number: Number) -> Number:
    def explode_helper(num: Number, curr_height: int) -> Number or None:
        if curr_height > 3:
            if not isinstance(num, int):
                return num
        if isinstance(num, int):
            return None
        left = explode_helper(num.left, curr_height + 1)
        return left if left else explode_helper(num.right, curr_height + 1)

    exploding_pair = explode_helper(number, 0)
    string_left, string_right = split_on_left_and_right_reduce_parts(exploding_pair, number)

    return string_number_to_number(
        explode_left(exploding_pair, string_left) + '0' + explode_right(exploding_pair, string_right))


def explode_right(exploding_pair: Number, right: str) -> str:
    for i in range(len(right)):
        if right[i].isnumeric():
            res_num = right[i]
            j = i + 1
            while j < len(right):
                if right[j].isnumeric():
                    res_num += right[j]
                    j += 1
                else:
                    break
            return right[:i] + str(int(res_num) + exploding_pair.right) + right[(i + len(res_num)):]
    return right


def explode_left(exploding_pair: Number, left: str) -> str:
    for i in reversed(range(len(left))):
        if left[i].isnumeric():
            j = i - 1
            res_num = left[i]
            while j > 0:
                if left[j].isnumeric():
                    res_num = left[j] + res_num
                    j -= 1
                    i -= 1
                else:
                    break
            return left[:i] + str(int(res_num) + exploding_pair.left) + left[(i + len(res_num)):]
    return left


def split_on_left_and_right_reduce_parts(exploding_pair: Number, number: Number) -> tuple[str, str]:
    string = str(number)
    deepness = 0
    for i, c in enumerate(list(string)):
        match c:
            case '[':
                deepness += 1
                if deepness >= 5:
                    return string[:i], string[i:].split(str(exploding_pair), 1)[1]
            case ']':
                deepness -= 1


def count_magnitude(number: Number) -> int:
    return number if isinstance(number, int) else 3 * count_magnitude(number.left) + 2 * count_magnitude(number.right)


def solution(file_name: str) -> int:
    numbers = read_input(file_name)
    res = numbers[0]
    for i in range(1, len(numbers)):
        res = add(res, numbers[i])
    return count_magnitude(res)


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME_1) == 143
    assert solution(TEST_FILE_NAME_2) == 1384
    assert solution(TEST_FILE_NAME_3) == 445
    assert solution(TEST_FILE_NAME_4) == 791
    assert solution(TEST_FILE_NAME_5) == 1137
    assert solution(TEST_FILE_NAME_6) == 3488
    assert solution(TEST_FILE_NAME_7) == 4140

    print(solution(FILE_NAME))
