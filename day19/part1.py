from collections import defaultdict

from day19 import *


def distance(first: Probe, second: Probe) -> Probe:
    return Probe(first.x - second.x, first.y - second.y, first.z - second.z, False)


def normalize_direction(normalized: Scanner, denormalized: Scanner) -> Scanner or None:
    distances: dict[Probe, int] = defaultdict(int)

    for normalized_probe in normalized.probes:
        for probe in denormalized.probes:
            distances[distance(normalized_probe, probe)] += 1

    if max(distances.values()) >= MINIMUM_COMMON:
        for k, v in distances.items():
            if v >= MINIMUM_COMMON:
                denormalized.distance = k
                return denormalized

    if denormalized.rotations_count == 23:
        denormalized.reset()
        return None

    denormalized.rotate()
    return normalize_direction(normalized, denormalized)


def normalize(normalized: Scanner, denormalized: Scanner) -> bool:
    res = normalize_direction(normalized, denormalized)
    if res is None:
        return False
    denormalized = res

    for probe in denormalized.probes:
        probe.x += denormalized.distance.x
        probe.y += denormalized.distance.y
        probe.z += denormalized.distance.z

    return True


def solution(file_name: str) -> int:
    scanners = read_input(file_name)
    normalize_all(scanners)

    all_probes = set()
    for scanner in scanners:
        for probe in scanner.probes:
            all_probes.add(str(probe))

    return len(all_probes)


def normalize_all(scanners: list[Scanner]) -> None:
    normalized_set = {find_zero_scanner(scanners)}
    denormalized_set = set(scanners).difference(normalized_set)

    while denormalized_set:
        denormalized = denormalized_set.pop()
        found = False
        for normalized in normalized_set:
            found = normalize(normalized, denormalized)
            if found:
                normalized_set.add(denormalized)
                break
        if not found:
            denormalized_set.add(denormalized)


def find_zero_scanner(scanners: list[Scanner]) -> Scanner:
    zero_scanner = None
    for scanner in scanners:
        if scanner.name == '0':
            zero_scanner = scanner
            break
    zero_scanner.distance = Probe(0, 0, 0)
    return zero_scanner


if __name__ == '__main__':
    assert solution(TEST_FILE_NAME) == 79

    print(solution(FILE_NAME))
