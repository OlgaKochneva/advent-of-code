import sys

def read_file(name: str):
    with open(name) as f:
        for line in f:
            yield line


def is_string_nice_1(line: str) -> bool:
    no_forbidden_substr = True # ab, cd, pq, xy
    has_repetitive_letters = False # aa, bb, cc

    vowels = 'aeiou'
    vowels_counter = 0
    forbidden_substrings = ['ab', 'cd', 'pq', 'xy']
    line_size = len(line)

    if line_size < 3: return False

    for i in range(line_size):
        if line[i] in vowels: vowels_counter += 1
        if line[i:i + 2] in forbidden_substrings: no_forbidden_substr = False
        if i != line_size - 1 and line[i] == line[i + 1]: has_repetitive_letters = True

    has_3_vowels = vowels_counter >= 3     
    
    return has_3_vowels and no_forbidden_substr and has_repetitive_letters
 

def is_string_nice_2(line: str) -> bool:
    condition_1 = False # contains pair of any two letters that appears at least twice in the string 
    condition_2 = False # contains one letter which repeats with exactly one letter between them
    line_size = len(line)

    if line_size < 4: return False

    condition_1_substr = {}
    for i in range(line_size):
        substr = line[i:i + 2]
        if substr in condition_1_substr:
            # check overlapping
            if i - condition_1_substr[substr] > 1:
                condition_1 = True
                break
        else:
            # save only leftmost index of substring so the aaaa or abab would work
            condition_1_substr[substr] = i

    for i in range(line_size - 2):
        substr = line[i:i + 3]
        if substr[0] == substr[-1]:
            condition_2 = True
            break   
    
    return condition_1 and condition_2


def get_nice_strings_number(f: callable, filename: str) -> int:
    counter = 0
    for line in read_file(filename):
        if f(line):
            counter += 1

    return counter


if __name__ == '__main__':
    filename = sys.argv[1]
    print('Nice strings number verified by 1-st method:', get_nice_strings_number(is_string_nice_1, filename))
    print('Nice strings number verified by 2-d method:', get_nice_strings_number(is_string_nice_2, filename))
