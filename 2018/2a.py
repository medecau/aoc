import sys

file_name = sys.argv[1]
two_counter = 0
three_counter = 0

with open(file_name) as input_file:
    for line in input_file:
        counter = dict()
        for char in line:
            try:
                counter[char] += 1
            except KeyError:
                counter[char] = 1

        if 2 in counter.values():
            two_counter += 1
        if 3 in counter.values():
            three_counter += 1

print(two_counter * three_counter)
