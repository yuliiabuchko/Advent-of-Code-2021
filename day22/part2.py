from day22 import *


class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def copy(self):
        return Point(self.x, self.y, self.z)


class Cuboid:
    def __init__(self, min_point: Point, max_point: Point):
        self.min_point = min_point
        self.max_point = max_point

    def is_valid(self):
        return self.min_point.x <= self.max_point.x \
               and self.min_point.y <= self.max_point.y \
               and self.min_point.z <= self.max_point.z

    def volume(self) -> int:
        return (self.max_point.x - self.min_point.x + 1) * \
               (self.max_point.y - self.min_point.y + 1) * \
               (self.max_point.z - self.min_point.z + 1)

    def __str__(self):
        return f'Min: {self.min_point}, Max: {self.max_point}'


def solution(file_name: str) -> int:
    lines = read_input(file_name)

    cuboids_list: list[Cuboid] = []

    for line in lines:
        new_cuboid = Cuboid(Point(line.x_start, line.y_start, line.z_start), Point(line.x_end, line.y_end, line.z_end))
        new_cuboids_list: list[Cuboid] = []

        for cuboid in cuboids_list:
            if not do_intersect(cuboid, new_cuboid):
                new_cuboids_list.append(cuboid)
                continue

            if cuboid.min_point.x <= new_cuboid.max_point.x <= cuboid.max_point.x:
                new_cuboids_list.append(
                    Cuboid(
                        Point(new_cuboid.max_point.x + 1, cuboid.min_point.y, cuboid.min_point.z),
                        cuboid.max_point.copy()
                    )
                )
                cuboid = Cuboid(cuboid.min_point, Point(new_cuboid.max_point.x, cuboid.max_point.y, cuboid.max_point.z))
            if cuboid.min_point.x <= new_cuboid.min_point.x <= cuboid.max_point.x:
                new_cuboids_list.append(
                    Cuboid(
                        cuboid.min_point.copy(),
                        Point(new_cuboid.min_point.x - 1, cuboid.max_point.y, cuboid.max_point.z)
                    )
                )
                cuboid = Cuboid(Point(new_cuboid.min_point.x, cuboid.min_point.y, cuboid.min_point.z), cuboid.max_point)

            if cuboid.min_point.y <= new_cuboid.max_point.y <= cuboid.max_point.y:
                new_cuboids_list.append(
                    Cuboid(
                        Point(cuboid.min_point.x, new_cuboid.max_point.y + 1, cuboid.min_point.z),
                        cuboid.max_point.copy()
                    )
                )
                cuboid = Cuboid(cuboid.min_point, Point(cuboid.max_point.x, new_cuboid.max_point.y, cuboid.max_point.z))
            if cuboid.min_point.y <= new_cuboid.min_point.y <= cuboid.max_point.y:
                new_cuboids_list.append(
                    Cuboid(
                        cuboid.min_point.copy(),
                        Point(cuboid.max_point.x, new_cuboid.min_point.y - 1, cuboid.max_point.z)
                    )
                )
                cuboid = Cuboid(Point(cuboid.min_point.x, new_cuboid.min_point.y, cuboid.min_point.z), cuboid.max_point)

            if cuboid.min_point.z <= new_cuboid.max_point.z <= cuboid.max_point.z:
                new_cuboids_list.append(
                    Cuboid(
                        Point(cuboid.min_point.x, cuboid.min_point.y, new_cuboid.max_point.z + 1),
                        cuboid.max_point.copy()
                    )
                )
                cuboid = Cuboid(cuboid.min_point, Point(cuboid.max_point.x, cuboid.max_point.y, new_cuboid.max_point.z))
            if cuboid.min_point.z <= new_cuboid.min_point.z <= cuboid.max_point.z:
                new_cuboids_list.append(
                    Cuboid(
                        cuboid.min_point.copy(),
                        Point(cuboid.max_point.x, cuboid.max_point.y, new_cuboid.min_point.z - 1)
                    )
                )

        if line.is_on:
            new_cuboids_list.append(new_cuboid)

        cuboids_list = new_cuboids_list

    return sum(cuboid.volume() for cuboid in cuboids_list)


def do_intersect(cuboid: Cuboid, new_cuboid: Cuboid) -> bool:
    return Cuboid(
        Point(max(cuboid.min_point.x, new_cuboid.min_point.x),
              max(cuboid.min_point.y, new_cuboid.min_point.y),
              max(cuboid.min_point.z, new_cuboid.min_point.z)),
        Point(min(cuboid.max_point.x, new_cuboid.max_point.x),
              min(cuboid.max_point.y, new_cuboid.max_point.y),
              min(cuboid.max_point.z, new_cuboid.max_point.z)),
    ).is_valid()


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME_SMALL) == 39
    assert solution(TEST_FILE_NAME_LARGEST) == 2758514936282235

    print(solution(FILE_NAME))
