from typing import Callable

from day05 import *


def in_different_segments(a: Point, b: Point, c: Point, d: Point, first: Line, second: Line) -> bool:
    return a in first and b in first and c in second and d in second


def get_common_line(first: Line, second: Line) -> Line or None:
    a, b, c, d = sorted([first.start, first.end, second.start, second.end],
                        key=None if first.direction() else Point.len_for_opposite_direction)
    if in_different_segments(a, b, c, d, first, second) or in_different_segments(a, b, c, d, second, first):
        if b != c:
            return None
    return Line(b, c)


def add_common_points(first: Line, second: Line, overlapped: set[Point]) -> None:
    if lines_are_parallel(first, second):
        if not lines_are_parallel(first, Line(first.start, second.start)):
            return
        common_line = get_common_line(first, second)
        if not common_line:
            return
        for point in common_line.all_points():
            overlapped.add(point)
        return
    p = intersection_point(first, second)
    if is_in_segment(p, first) and is_in_segment(p, second):
        overlapped.add(p)


def filter_input(lines: list[Line]) -> list[Line]:
    res = []
    for line in lines:
        if line.is_horizontal() or line.is_vertical():
            res.append(line)
    return res


def solution(file_name: str, filter_function: Callable[[list[Line]], list[Line]]) -> int:
    lines = filter_function(read_input(file_name))
    overlapped = set()
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            add_common_points(lines[i], lines[j], overlapped)
    return len(overlapped)


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME, filter_input) == 5

    print(solution(FILE_NAME, filter_input))
