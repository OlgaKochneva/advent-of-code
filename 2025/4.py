"""Lazy solution: using deepcopy and repeating the algorithm of checking neighbours more than necessary
meaning we don't check if something changed after we removed a neighbour and just start algorithm anew.

For example it takes 99 iteration for 2 part and the delay is visible. The solution 4_alternative.py fixes that problem.
I left the two solutions in folder because I have a free will and I do whatever I want. 
"""

from util import *
import copy

def check_neighbours(i: int, j: int, data: list[list[str]]) -> bool:
    neighbours = 8
    check_idx = [
        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
        (i, j - 1), (i, j + 1),
        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
    
    for i, j in check_idx:
        if i < 0 or i == len(data) or j < 0 or j == len(data[i]):
            neighbours -= 1
        elif data[i][j] == '.':
            neighbours -= 1
        
        if neighbours < 4:
            break
    
    return neighbours < 4
    

def accessible_cargo(data: list[list[str]]) -> int:
    result = 0
    new_data = copy.deepcopy(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '@':
                if check_neighbours(i, j, data):
                    result += 1
                    new_data[i][j] = '.'
    
    return result, new_data


if __name__ == '__main__':
    data = [list(line.strip()) for line in read_file(TASK_FILENAME)]

    removed, data = accessible_cargo(data)
    print('Accessible cargo', removed)
    
    total_removed = removed
    while removed != 0:
        removed, data = accessible_cargo(data)
        total_removed += removed
    
    print('Total removed cargo', total_removed)
