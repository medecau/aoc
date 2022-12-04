import sys

file_path = sys.argv[1]
frequency = 0

with open(file_path) as input_file:
    for line in input_file:
        sign, num = line[0], int(line[1:])
        if sign == "+":
            frequency += num
        elif sign == "-":
            frequency -= num

print(frequency)
