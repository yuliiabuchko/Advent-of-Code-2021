FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'

EPSILON: float = 0.000001


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return distance(self, Point(0, 0)) < distance(other, Point(0, 0))

    def __hash__(self):
        return hash(str(self))

    def len_for_opposite_direction(self) -> float:
        return distance(self, Point(0, 1000))


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def is_diagonal(self) -> bool:
        return abs(self.start.x - self.end.x) == abs(self.start.y - self.end.y)

    def direction(self) -> bool:
        """
        :return: True if direction from left bottom to right top, False otherwise
        """
        return (self.start.x - self.end.x) * (self.start.y - self.end.y) > 0

    def all_points(self) -> list[Point]:
        x_delta = self.get_delta(self.start.x, self.end.x)
        y_delta = self.get_delta(self.start.y, self.end.y)

        res = []
        curr = self.start
        while curr != self.end:
            res.append(curr)
            curr = Point(curr.x + x_delta, curr.y + y_delta)
        res.append(self.end)
        return res

    @staticmethod
    def get_delta(start: int, end: int) -> int:
        if start > end:
            return -1
        if start < end:
            return 1
        return 0

    def length(self) -> float:
        return ((self.start.x - self.end.x) ** 2 + (self.start.y - self.end.y) ** 2) ** (1 / 2)

    def __contains__(self, item):
        return self.start == item or self.end == item

    def __str__(self):
        return f'{self.start} -> {self.end}'


def distance(first: Point, second: Point) -> float:
    dist = ((first.x - second.x) ** 2 + (first.y - second.y) ** 2) ** (1 / 2)
    return dist


def is_in_segment(point: Point, segment: Line) -> bool:
    return abs(distance(point, segment.start) + distance(point, segment.end) - segment.length()) < EPSILON


def lines_are_parallel(first: Line, second: Line) -> bool:
    return product(first, second) == 0


def product(first: Line, second: Line) -> int:
    return (first.start.x - first.end.x) * (second.start.y - second.end.y) - \
           (first.start.y - first.end.y) * (second.start.x - second.end.x)


def intersection_point(first: Line, second: Line) -> Point:
    div = product(first, second)
    first_ = first.start.x * first.end.y - first.start.y * first.end.x
    second_ = second.start.x * second.end.y - second.start.y * second.end.x

    x = first_ * (second.start.x - second.end.x) - (first.start.x - first.end.x) * second_
    y = first_ * (second.start.y - second.end.y) - (first.start.y - first.end.y) * second_

    return Point(x // div, y // div)


def read_input(file_name: str) -> list[Line]:
    with open(file_name) as file:
        res = []
        for line in file.readlines():
            start, end = line.strip().split(' -> ')
            start_x, start_y = start.split(',')
            end_x, end_y = end.split(',')
            res.append(Line(Point(int(start_x), int(start_y)), Point(int(end_x), int(end_y))))
        return res
