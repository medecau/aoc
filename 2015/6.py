from utils import get_input
import itertools


instructions = get_input('6.txt').split('\n')
matrix = [[0] * 1000] * 1000
matrix = map(list, matrix)
for i in instructions:
    parts = i.split(' ')
    origin, destiny = parts[-3], parts[-1]
    origin = map(int, parts[-3].split(','))
    destiny = map(int, parts[-1].split(','))
    for x in range(origin[0], destiny[0] + 1):
        for y in range(origin[1], destiny[1] + 1):
            if parts[0] == 'toggle':
                matrix[x][y] += 2
            elif parts[0] == 'turn':
                if parts[1] == 'on':
                    matrix[x][y] += 1
                elif matrix[x][y] > 0:
                    matrix[x][y] -= 1
flat = list(itertools.chain(*matrix))

print(sum(flat))
