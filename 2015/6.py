from utils import get_input, lmap
import itertools


instructions = get_input('6.txt').split('\n')
matrix = [[0] * 1000] * 1000
matrix = lmap(list, matrix)
for i in instructions:
    parts = i.split(' ')
    origin, destination = parts[-3], parts[-1]
    ox, oy = map(int, origin.split(','))
    dx, dy = map(int, destination.split(','))
    for x in range(ox, dx + 1):
        for y in range(oy, dy + 1):
            if parts[0] == 'toggle':
                matrix[x][y] += 2
            elif parts[0] == 'turn':
                if parts[1] == 'on':
                    matrix[x][y] += 1
                elif matrix[x][y] > 0:
                    matrix[x][y] -= 1
flat = list(itertools.chain(*matrix))

print(sum(flat))
