FILE_NAME: str = 'input.txt'
TEST_FILE_NAME: str = 'test_input.txt'

MINIMUM_COMMON: int = 12


class Probe:
    def __init__(self, x: int, y: int, z: int, count_rotations: bool = True):
        self.x = x
        self.y = y
        self.z = z

        self.all_rotations = [] if not count_rotations else self.get_all_rotations()

    def rotate(self, rotation_index: int) -> None:
        self.x, self.y, self.z = self.all_rotations[rotation_index]

    def get_all_rotations(self) -> list[tuple[int, int, int]]:
        rotations = []

        def rotation_helper(x, y, z):
            rotations.append((x, y, z))
            rotations.append((x, -z, y))
            rotations.append((x, -y, -z))
            rotations.append((x, z, -y))
            rotations.append((-x, -y, z))
            rotations.append((-x, z, y))
            rotations.append((-x, y, -z))
            rotations.append((-x, -z, -y))

        rotation_helper(self.x, self.y, self.z)
        rotation_helper(self.y, self.z, self.x)
        rotation_helper(self.z, self.x, self.y)
        return rotations

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash(str(self))


class Scanner:
    def __init__(self, name: str, probes: set[Probe]):
        self.name = name
        self.probes = probes
        self.rotations_count = 0
        self.distance = None

    def rotate(self):
        self.rotations_count += 1
        for probe in self.probes:
            probe.rotate(self.rotations_count)

    def reset(self):
        self.rotations_count = -1
        self.rotate()

    def __str__(self):
        return self.name


def read_input(file_name: str) -> list[Scanner]:
    res = []
    with open(file_name) as file:
        curr_scanner_num = None
        curr_probes = set()
        for line in file.readlines():
            if line.startswith('---'):
                curr_scanner_num = line.split()[2]
            elif not line.strip():
                res.append(Scanner(curr_scanner_num, curr_probes))
                curr_probes = set()
            else:
                x, y, z = line.strip().split(',')
                curr_probes.add(Probe(int(x), int(y), int(z)))
        res.append(Scanner(curr_scanner_num, curr_probes))
    return res
