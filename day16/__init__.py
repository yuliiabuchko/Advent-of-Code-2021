FILE_NAME: str = 'input.txt'

TEST_FILE_NAME_PART_1_01: str = 'test_input_part_1_01.txt'
TEST_FILE_NAME_PART_1_02: str = 'test_input_part_1_02.txt'
TEST_FILE_NAME_PART_1_03: str = 'test_input_part_1_03.txt'
TEST_FILE_NAME_PART_1_04: str = 'test_input_part_1_04.txt'
TEST_FILE_NAME_PART_1_05: str = 'test_input_part_1_05.txt'
TEST_FILE_NAME_PART_1_06: str = 'test_input_part_1_06.txt'
TEST_FILE_NAME_PART_1_07: str = 'test_input_part_1_07.txt'

TEST_FILE_NAME_PART_2_01: str = 'test_input_part_2_01.txt'
TEST_FILE_NAME_PART_2_02: str = 'test_input_part_2_02.txt'
TEST_FILE_NAME_PART_2_03: str = 'test_input_part_2_03.txt'
TEST_FILE_NAME_PART_2_04: str = 'test_input_part_2_04.txt'
TEST_FILE_NAME_PART_2_05: str = 'test_input_part_2_05.txt'
TEST_FILE_NAME_PART_2_06: str = 'test_input_part_2_06.txt'
TEST_FILE_NAME_PART_2_07: str = 'test_input_part_2_07.txt'
TEST_FILE_NAME_PART_2_08: str = 'test_input_part_2_08.txt'


def read_input(file_name: str) -> str:
    with open(file_name) as file:
        return ''.join(bin(int(c, 16))[2:].rjust(4, '0') for c in list(file.readline().strip()))
