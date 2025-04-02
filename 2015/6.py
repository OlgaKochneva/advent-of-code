import sys
from collections import namedtuple

coord = namedtuple('coord', ['x', 'y'])


def read_file(name: str):
    with open(name) as f:
        for line in f:
            yield line


def parse_commands(cmd_lines: list[str], wrong_mode: False) -> list[(callable, coord, coord)]:
    """Parses command lines provided in one of the following formats:
        turn on {int},{int} through {int},{int}
        turn off {int},{int} through {int},{int} 
        toggle {int},{int} through {int},{int}
    
        into to a list of commands and coordinats
        the command which is a callable (lambda) depends on the passed mode:

        wrong_mode: True - corresponds to the part 1 of the task
            turn off -> x and 0
            turn on -> x or 1
            toggle ->  x ^ 1 (logical xor)

        wrong_mode: False - corresponds to the part 2 of the task and becomes a default behaviour
            turn off -> x - 1 (with the extra check for x > 0)
            turn on -> x + 1
            toggle ->  x + 2 
    """
    commands = []
    parse_numbers = lambda l: coord(int(l.split(',')[0]), int(l.split(',')[1]))
    for line in read_file(filename):
        line = line.split()
        if line[0] == 'turn':
            if wrong_mode:
                # for the part 1 of the task
                cmd = (lambda x: x and 0) if line[1] == 'off' else (lambda x: x or 1)
            else:
                # for the part 2 of the task
                if line[1] == 'off':
                    cmd = lambda x: x - 1 if x > 0 else 0
                else:
                    cmd = lambda x: x + 1

            start = parse_numbers(line[2])
        else: # means that we recieved 'toggle' command
            cmd = (lambda x: x ^ 1) if wrong_mode else (lambda x: x + 2)
            start = parse_numbers(line[1])
        
        end = parse_numbers(line[-1])
        commands.append((cmd, start, end))

    return commands
 

def count_lights(commands: list[(callable, coord, coord)]) -> int:
    grid = [[0] * 1000 for _ in range(1000)]
    for cmd, start, end in commands:
        for y in range(start.y, end.y + 1):
            for x in range(start.x, end.x + 1):
                grid[y][x] = cmd(grid[y][x])
            
    return sum([sum(grid[i]) for i in range(1000)])


if __name__ == '__main__':
    filename = sys.argv[1]
    commands = parse_commands(filename, True)
    print('Number of turned on lights (part 1): ', count_lights(commands))
    commands = parse_commands(filename, False)
    print('Brightness of lights (part 2): ', count_lights(commands))
