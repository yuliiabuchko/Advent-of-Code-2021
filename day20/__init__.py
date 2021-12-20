FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'

INF_COUNT = 150
SAFE_DISTANCE = 60


def read_input(file_name: str) -> tuple[list[chr], list[list[chr]]]:
    with open(file_name) as file:
        algorithm = list(file.readline().strip())
        file.readline()

        size = None
        image = []
        for line in file.readlines():
            size = len(line) + 2 * INF_COUNT
            image.append(list('.' * INF_COUNT) + list(line.strip()) + list('.' * INF_COUNT))

        for _ in range(INF_COUNT):
            image.insert(0, list('.' * size))
            image.append(list('.' * size))

        return algorithm, image
