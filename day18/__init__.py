FILE_NAME: str = 'input.txt'
TEST_FILE_NAME_1: str = 'test_input_1.txt'
TEST_FILE_NAME_2: str = 'test_input_2.txt'
TEST_FILE_NAME_3: str = 'test_input_3.txt'
TEST_FILE_NAME_4: str = 'test_input_4.txt'
TEST_FILE_NAME_5: str = 'test_input_5.txt'
TEST_FILE_NAME_6: str = 'test_input_6.txt'
TEST_FILE_NAME_7: str = 'test_input_7.txt'


class Number:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f'[{str(self.left)},{str(self.right)}]'


def string_number_to_number(line: str) -> Number:
    stack_numbers = []
    for i, c in enumerate(list(line)):
        match c:
            case '[':
                stack_numbers.append(Number(None, None))
            case ',':
                tmp = stack_numbers.pop()
                curr = stack_numbers.pop()
                curr.left = tmp
                stack_numbers.append(curr)
            case ']':
                tmp = stack_numbers.pop()
                curr = stack_numbers.pop()
                curr.right = tmp
                stack_numbers.append(curr)
            case _:
                if line[i - 1].isnumeric():
                    prev = stack_numbers.pop()
                    stack_numbers.append(int(c) + 10 * prev)
                else:
                    stack_numbers.append(int(c))

    return stack_numbers.pop()


def read_input(file_name: str) -> list[Number]:
    res = []
    with open(file_name) as file:
        for line in file.readlines():
            res.append(string_number_to_number(line.strip()))
    return res
