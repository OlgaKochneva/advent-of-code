from util import *

    
def output_joltage(data: list[str], batteries_number: int) -> int:
    result = 0
    for line in data:
        number = ['0'] * batteries_number
        j = 0 # current index in resulting number
        k = 0 # currrent index in line
        total_batteries = len(line)
        while j < batteries_number:
            for i in range(k, total_batteries - batteries_number + j + 1):
                if number[j] < line[i]:
                    number[j] = line[i]
                    k = i + 1
            
            j += 1

        result += int(''.join(number))
    
    return result


if __name__ == '__main__':
    data = [line.strip() for line in read_file(TASK_FILENAME)]
    print('Output joltage for 2 =', output_joltage(data, 2))
    print('Output joltage for 12 =', output_joltage(data, 12))
