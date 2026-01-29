
"""SMART solution: creating an additional grid that shows how many neighbours current item has, 
when we remove the item, we have to reduce the amount of neighbours for each neighbour of this item,
by doing that we can reduce the amount of iterations for the 2d part and when we go for the next iteration 
we dont have to count neighbours, because we already did it.

For example it takes 69 iteration for 2 part and no delay in comparison with 4.py solution.
"""

from util import *


def count_neighbours(i: int, j: int, data: list[list[str]]) -> int:
    """Returns amount of neighbours for (i, j) roll."""
    neighbours = 0
    
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue

            if 0 <= i + di < len(data) and 0 <= j + dj < len(data[i + di]) and data[i + di][j + dj] == '@':
                neighbours += 1

    return neighbours


def make_accessibility_grid(data: list[list[str]]) -> list[list[int]]:
    """Creates map(grid) where (i,j) is the roll coordinates and value is amount of roll's neighbours."""
    grid = []

    for i, line in enumerate(data):
        grid.append([-1] * len(line))
        for j, item in enumerate(line):
            if item == '@':
                grid[i][j] = count_neighbours(i, j, data)

    return grid


def recalculate_neighbours(i: int, j: int, grid: list[list[int]]):
    """Update amount of neighbours for each neighbour of roll (i,j) after removing."""
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue

            if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[i + di]):
                grid[i + di][j + dj] -= 1


def get_removable_amount(grid: list[list[int]], insta_remove: bool = False):
    """Get amount of rolls accessible for removal.
    
    insta_remove: imitates removal of accessible roll and proceeding without it
    """
    removable_amount = 0
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if 0 <= item < 4:
                removable_amount += 1
                if insta_remove:
                    grid[i][j] = -1 # remove roll
                    recalculate_neighbours(i, j, grid)

    return removable_amount


if __name__ == '__main__':
    data = [list(line.strip()) for line in read_file(TASK_FILENAME)]
    accessibility_grid = make_accessibility_grid(data)
    
    print("#1 Amount of removable rolls in first run:", get_removable_amount(accessibility_grid))

    total_removable_amount = 0
    removable_amount = get_removable_amount(accessibility_grid, True) 
    while removable_amount != 0:
        total_removable_amount += removable_amount
        removable_amount = get_removable_amount(accessibility_grid, True) 

    print("#2 Total amount of removable rolls:", total_removable_amount)
