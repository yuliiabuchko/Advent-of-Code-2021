FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'


class Dot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def fold_y(self, y: int):
        if self.y > y:
            self.y = self.y - 2 * (self.y - y)

    def fold_x(self, x: int):
        if self.x > x:
            self.x = self.x - 2 * (self.x - x)

    def fold(self, axis: str, number: int):
        if axis == 'x':
            self.fold_x(number)
        else:
            self.fold_y(number)

    def __str__(self):
        return f'({self.x},{self.y})'

    def __hash__(self):
        return hash(self.x * self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def read_input(file_name: str) -> tuple[set[Dot], list[tuple[str, int]]]:
    dots = set()
    folds = []
    with open(file_name) as file:
        for line in file.readlines():
            if line == "\n":
                continue
            if line.startswith("fold"):
                _, _, dest = line.strip().split()
                axis, number = dest.split('=')
                folds.append((axis, int(number)))
                continue
            x, y = line.strip().split(',')
            dots.add(Dot(int(x), int(y)))
    return dots, folds
