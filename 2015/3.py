import sys
from collections import namedtuple, defaultdict

filename = sys.argv[1]


def read_file(name: str):
    with open(name) as f:
        for symb in f.read():
            yield symb

coord = namedtuple('coord', ['x', 'y'])
instr2coord = {'>': coord(1, 0), '<': coord(-1, 0), '^': coord(0, 1), 'v': coord(0, -1)}
update_coord = lambda a, b: coord(a.x + b.x, a.y + b.y)

def solo_santa_job_results() -> int:
    current_point = coord(0, 0)
    res = defaultdict(int)
    res[current_point] = 1
    for instruction in read_file(filename):
        current_point = update_coord(current_point, instr2coord[instruction])
        res[current_point] += 1

    return len(res)

def robot_and_santa_job_results() -> int:
    current_point = current_robopoint = current_santapoint = coord(0, 0)
    res = defaultdict(int)
    res[current_point] = 2
    
    for i, instruction in enumerate(read_file(filename)):
        if i % 2:
            current_point = current_santapoint = update_coord(current_santapoint, instr2coord[instruction])
        else:
            current_point = current_robopoint = update_coord(current_robopoint, instr2coord[instruction])

        res[current_point] += 1

    return len(res)


if __name__ == '__main__':
    print('Solo Santa delivery results:', solo_santa_job_results())
    print('Santa + Robot delivery results:', robot_and_santa_job_results())