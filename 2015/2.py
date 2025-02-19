import sys

filename = sys.argv[1]

def read_file(name: str):
    with open(name) as f:
        for line in f:
            # just sort right now to know the two shortest sides
            yield tuple(sorted(int(num) for num in line.split('x')))


def calculate_materials() -> tuple[int, int]:
    wrapping_paper_area = 0
    ribbon_length = 0
    for s1, s2, s3 in read_file(filename):
        # box size
        wrapping_paper_area += 2 * (s1 * s2 + s2 * s3 + s3 * s1)
        # slack size
        wrapping_paper_area += s1 * s2

        ribbon_length += 2 * (s1 + s2) + s1 * s2 * s3


    return wrapping_paper_area, ribbon_length


if __name__ == '__main__':
    print('Wrapping paper area: {}\nRibbon length: {}'.format(*calculate_materials()))