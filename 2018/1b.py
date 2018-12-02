import sys
import itertools


file_path = sys.argv[1]
frequency = 0
seen = set()

with open(file_path) as input_file:
    for line in itertools.cycle(input_file):
        sign, num = line[0], int(line[1:])
        if sign == '+':
            frequency += num
        elif sign == '-':
            frequency -= num
        if frequency not in seen:
            seen.add(frequency)
        else:
            break

print(frequency)
