import sys

filename = sys.argv[1]

# Part 1
floor = 0
with open(filename) as f:
    for letter in f.read():
        if letter == '(':
            floor += 1
        else:
            floor -= 1

print('Floor: ', floor)


# Part 2
floor = 0
with open(filename) as f:
    for i, letter in enumerate(f.read(), 1):
        if letter == '(':
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            print('Basement instruction', i)
            break
