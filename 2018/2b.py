import sys


file_name = sys.argv[1]

lines = tuple(l.strip() for l in open(file_name))

for left_line_index, left_line in enumerate(lines[:-1]):
    for right_line in lines[left_line_index + 1:]:
        diff_char_counter = 0
        diff_idx = set()
        for idx in range(len(left_line)):
            if left_line[idx] != right_line[idx]:
                diff_char_counter += 1
                diff_idx.add(idx)
        if diff_char_counter == 1:
            diff_idx = tuple(diff_idx)
            print('{}{}'.format(left_line[0:diff_idx[0]], left_line[diff_idx[0] + 1:]))

