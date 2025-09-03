import sys
from functools import cache
from collections import namedtuple

from util import read_file

COMMAND_MAPPING = {
    'ASSIGMENT': lambda x: x,
    'NOT': lambda x:  ~x,
    'RSHIFT': lambda x, n: x >> n,
    'LSHIFT': lambda x, n: x << n,
    'AND': lambda x, y: x & y,
    'OR': lambda x, y: x | y,
}

instruction = namedtuple('instruction', ['op', 'args'])

def parse_circuit(instructions: list[str]) -> dict[str, instruction]:
    """Parse raw text lines into more convenient instructions."""
    parsed_instructions = {}
    for line in instructions:
        line = line.split()
        wire_name = line[-1]
        if len(line) == 3: # assigment
            op = 'ASSIGMENT'
            args = (line[0], None)
        elif len(line) == 4: # NOT   
            op = 'NOT'
            args = (line[1], None)
        else: # two args functions
            op = line[1]
            args = (line[0], line[2])

        parsed_instructions[wire_name] = instruction(op, args)

    return parsed_instructions

@cache
def run_commands(wire_name: str) -> int:
    """Execute instructions to calculate signals. Calculated signals saved into functions cache
    
    * assumed that instructions are stored in global namespace, 
      not passing into function for 'cache' annotation usage
    """
    op = instructions[wire_name].op
    arg_1, arg_2 = instructions[wire_name].args

    if arg_1.isnumeric():
        arg_1 = int(arg_1)
    else:
        arg_1 = run_commands(arg_1)

    if op == 'ASSIGMENT' or op == 'NOT': # if it is a one argument operation
        return COMMAND_MAPPING[op](arg_1)
    else:
        if arg_2.isnumeric():
            arg_2 = int(arg_2)
        else:
            arg_2 = run_commands(arg_2)

        return COMMAND_MAPPING[op](arg_1, arg_2)
    

if __name__ == '__main__':
    cmd_lines = read_file(sys.argv[1])

    # part 1
    instructions = parse_circuit(cmd_lines)
    res_wire = run_commands('a')
    print('Wire "a" = ', res_wire)

    # part 2
    instructions['b'] = instruction('ASSIGMENT', (str(res_wire), None))
    run_commands.cache_clear()
    res_wire = run_commands('a')
    
    print('Wire "a" = ', res_wire)
