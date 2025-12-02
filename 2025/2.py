from math import log10
from util import *


def invalid_id_sum_1(data: list[tuple[int]]) -> int:
    """Generating invalid number and check if it is included in interval. No string operations."""
    invalid_id_sum = 0
    dgt_number = lambda x: int(log10(x)) + 1
    for start, end in data:
        n = start
        while n < end:
            n_dgt_number = dgt_number(n)
            if n_dgt_number % 2: # есть нечетное то скипаем
                n += 1
                continue
            
            mirror_number = n // 10 ** (n_dgt_number // 2)
            mirror_number = mirror_number * 10 ** (n_dgt_number // 2) + mirror_number
            
            if mirror_number <= end:
                if mirror_number >= n:
                    invalid_id_sum += mirror_number
                    n = mirror_number

            n += 1
    
    return invalid_id_sum


def invalid_id_sum_2(data: list[tuple[int]]) -> int:
    """Checking each number if it is invalid. NOT OPTIMAL AT ALL"""
    invalid_id_sum = 0

    for start, end in data:
        for n in range(start, end + 1):
            n = str(n)
            for chunk in range(1, len(n)//2 + 1):
                if n == n[:chunk] * (len(n) // chunk):
                    invalid_id_sum += int(n)
                    break
    
    return invalid_id_sum


if __name__ == '__main__':
    data = [line.split('-') for line in read_file(TASK_FILENAME)[0].split(',')]
    data = [(int(line[0]), int(line[1])) for line in data]
    print('#1 Invalid id sum =', invalid_id_sum_1(data))
    print('#2 Invalid id sum =', invalid_id_sum_2(data))
