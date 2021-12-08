from day08 import *


def solve_pattern(entry: Entry) -> dict[chr, chr]:
    result = dict()
    set_one = [s for s in entry.patterns if len(s) == len(Number.ONE)][0]
    set_four = [s for s in entry.patterns if len(s) == len(Number.FOUR)][0]
    set_seven = [s for s in entry.patterns if len(s) == len(Number.SEVEN)][0]
    set_eight = [s for s in entry.patterns if len(s) == len(Number.EIGHT)][0]

    result[set_seven.difference(set_one).pop()] = 'a'
    bd = set_four.difference(set_one)
    cde = _get_cde(entry)
    de = cde.difference(set_one)
    d = bd.intersection(de).pop()
    result[d] = 'd'
    result[bd.difference(d).pop()] = 'b'
    result[de.difference(bd).pop()] = 'e'
    c = cde.difference(de).pop()
    result[c] = 'c'
    result[set_one.difference(c).pop()] = 'f'
    result[set_eight.difference(set(result.keys())).pop()] = 'g'

    return result


def _get_cde(entry: Entry) -> set[chr]:
    t = dict()
    for pattern in entry.patterns:
        if len(pattern) == 6:
            for c in pattern:
                if c not in t:
                    t[c] = 0
                t[c] += 1
    cde = set()
    for k, v in t.items():
        if v == 2:
            cde.add(k)
    return cde


def get_number_from_pattern(mapping: dict[chr, chr], output: set) -> int:
    transformed = set()
    for char in output:
        transformed.add(mapping[char])
    for number in Number.all_numbers():
        if transformed == number.value:
            return int(number)


def solve(entry: Entry) -> int:
    mapping = solve_pattern(entry)
    res = ''
    for out in entry.output:
        res += str(get_number_from_pattern(mapping, out))
    return int(res)


def solution(file_name: str) -> int:
    entries = read_input(file_name)
    return sum(map(solve, entries))


if __name__ == '__main__':
    assert solution(TEST_SMALL_FILE_NAME) == 5353
    assert solution(TEST_FILE_NAME) == 61229

    print(solution(FILE_NAME))
