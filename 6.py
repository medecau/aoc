from utils import get_input
import itertools


instructions = get_input('6.txt').split('\n')

matrix = [[False] * 1000] * 1000
matrix = map(list, matrix)
for i in instructions:
    parts = i.split(' ')
    origin, destiny = parts[-3], parts[-1]
    origin = map(int, parts[-3].split(','))
    destiny = map(int, parts[-1].split(','))
    for x in range(origin[0], destiny[0] + 1):
        for y in range(origin[1], destiny[1] + 1):
            if parts[0] == 'toggle':
                matrix[x][y] = not matrix[x][y]
            elif parts[0] == 'turn':
                if parts[1] == 'on':
                    matrix[x][y] = True
                else:
                    matrix[x][y] = False
flat = list(itertools.chain(*matrix))
print(len([h for h in flat if h is True]))
