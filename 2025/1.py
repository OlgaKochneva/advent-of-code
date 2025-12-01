from util import *


def cmd_parser(filename: str) -> list[tuple[int, int]]:
    cmds = []
    for line in read_file(filename):
        cmds.append((
           1 if line.startswith('R') else -1,
           int(line[1:])
        ))
    
    return cmds


def endzero_counter(cmds: list[tuple[int, int]], start_pos=50) -> int:
    counter = 0
    pos = start_pos
    for direction, num in cmds:
        pos = (pos + direction * num) % 100
        if pos == 0:
            counter += 1

    return counter


def passzero_counter(cmds: list[tuple[int, int]], start_pos=50) -> int:
    counter = 0
    pos = start_pos
    for direction, num in cmds:
        if direction == 1:
            pos += num
            if pos >= 100: # we did a zero pass
                counter += pos // 100 # but how many passes we did?  
        else:
            extra_inc = 0 if pos == 0 else 1 # so we dont count twice the zero pass if we start from it
            pos -= num
            if pos <= 0:
                counter += abs(pos) // 100 + extra_inc

        pos %= 100

    return counter

if __name__ == '__main__':
    cmds = cmd_parser(TASK_FILENAME)

    print('#1 Code =', endzero_counter(cmds))
    print('#2 Code =', passzero_counter(cmds))
