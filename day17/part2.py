from day17 import *
from day17.part1 import Probe, probe_cannot_reach, reached


def solution(file_name: str) -> int:
    x_min, x_max, y_min, y_max = read_input(file_name)
    probes = set()
    for x in range(250):
        for y in range(-250, 250):
            p = Probe(x, y)
            while not probe_cannot_reach(p, x_max, y_min):
                p.move()
                if reached(p, x_min, x_max, y_min, y_max):
                    probes.add((x, y))
                    break
    return len(probes)


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 112

    print(solution(FILE_NAME))
