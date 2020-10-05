from utils import get_input

moves = get_input('3.txt')

x, y = 0, 0
log = [tuple([x, y])]
for move in moves:
    if move == '^':
        y += 1
    elif move == 'v':
        y -= 1
    elif move == '<':
        x -= 1
    elif move == '>':
        x += 1
    log.append(tuple([x, y]))

houses = ['%dx%d' % h for h in log]
unique_houses = set(houses)
print(len(unique_houses))


santa = dict(x=0, y=0, log=[tuple([0, 0])])
robot = dict(x=0, y=0, log=[tuple([0, 0])])

queue = [santa, robot]
for move in moves:
    current = queue.pop(0)
    queue.append(current)
    if move == '^':
        current['y'] += 1
    elif move == 'v':
        current['y'] -= 1
    elif move == '<':
        current['x'] -= 1
    elif move == '>':
        current['x'] += 1
    current['log'].append(tuple([current['x'], current['y']]))

santa_houses = ['%dx%d' % h for h in santa['log']]
robot_houses = ['%dx%d' % h for h in robot['log']]
unique_houses = set(santa_houses) | set(robot_houses)
print(len(unique_houses))
