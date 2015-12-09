from utils import get_input
import itertools


lines = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""".splitlines()

lines = get_input('9.txt').splitlines()

pairs = [l.split(' = ') for l in lines]
pairs = [tuple([sorted(c.split(' to ')), d]) for c, d in pairs]

all_cities = [cities[0] for cities, distance in pairs]
all_cities += [cities[1] for cities, distance in pairs]
all_cities = set(all_cities)

permutations = itertools.permutations(all_cities, len(all_cities))

distances = list()
for p in permutations:
    current = 0
    for i in range(len(p) - 1):
        pair = sorted(p[i:i + 2])
        for e in pairs:
            if pair == e[0]:
                distance = e[1]
                break
        current += int(distance)
    distances.append(current)

print min(distances), max(distances)
