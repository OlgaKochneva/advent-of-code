import sys

from typing import Iterable

from util import read_file

def calculation_p1(lines: Iterable) -> tuple[int, int]:
    """Calculates the difference between the number of characters in the code representation of the string literal
    and the number of characters in the in-memory string itself.
    """
    code = 0
    char = 0
    for line in lines:
        code += len(line)
        # starting with 1 and ending with line - 1 to skip ""
        i = 1
        while i < len(line) - 1:
            if line[i] == '\\':
                i += 1
                if line[i] == 'x':
                    i += 2

            char += 1
            i += 1


    return code - char, code

def calculation_p2(lines: Iterable, subpr_p1: int) -> int:
    """Calculates the number of characters of code for string literals minus the number of characters
    in memory for the values of the strings
    """
    code = 0
    for line in lines:
        i = 0
        while i < len(line):
            if line[i] == '\\' or line[i] == '"':
                code += 1

            i += 1
            code += 1

        code += 2

    return code - subpr_p1


if __name__ == '__main__':
    lines = [line.rstrip() for line in read_file(sys.argv[1])] # remove \n from lines

    res1, subproduct1 = calculation_p1(lines)
    print('Part 1 result: ', res1)
    res2 = calculation_p2(lines, subproduct1)
    print('Part 2 result: ', res2)
