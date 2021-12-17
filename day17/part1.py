from day17 import *


class Probe:
    def __init__(self, x_velocity: int, y_velocity: int):
        self.x = 0
        self.y = 0

        self.velocity_x = x_velocity
        self.velocity_y = y_velocity

    def move(self) -> None:
        self.x += self.velocity_x
        self.y += self.velocity_y

        if self.velocity_x > 0:
            self.velocity_x -= 1
        elif self.velocity_x < 0:
            self.velocity_x += 1

        self.velocity_y -= 1


def probe_cannot_reach(probe: Probe, x_max: int, y_min: int) -> bool:
    return probe.x > x_max or probe.y < y_min


def reached(probe: Probe, x_min: int, x_max: int, y_min: int, y_max: int) -> bool:
    return x_min <= probe.x <= x_max and y_min <= probe.y <= y_max


def solution(file_name: str) -> int:
    x_min, x_max, y_min, y_max = read_input(file_name)
    highest = 0
    for x in range(250):
        for y in range(250):
            p = Probe(x, y)
            max_pos_y = p.y
            while not probe_cannot_reach(p, x_max, y_min):
                p.move()
                max_pos_y = max(max_pos_y, p.y)
                if reached(p, x_min, x_max, y_min, y_max):
                    highest = max(highest, max_pos_y)
                    break
    return highest


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 45

    print(solution(FILE_NAME))
