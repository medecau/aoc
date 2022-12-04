import re
from collections import defaultdict
from itertools import permutations

import utils

instructions = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.""".splitlines()

instructions = utils.get_lines(__file__)

pattern = re.compile(
    r"(?P<sub>.*) would (?P<type>lose|gain) (?P<qty>\d+) .* to (?P<obj>[^\.]+)"
)

graph = defaultdict(defaultdict)
for i in instructions:
    match = pattern.match(i).groupdict()
    qty = int(match["qty"])
    if match["type"] == "lose":
        qty *= -1
    graph[match["sub"]][match["obj"]] = qty

roster = graph.keys()

for each in roster:
    graph[each]["me"] = 0

graph["me"] = {k: 0 for k in roster}

roster = graph.keys()

best = None
for p in permutations(roster):
    change = 0
    for i in range(len(p)):
        sub = p[i]
        left = p[i - 1]
        right = p[i + 1] if i + 1 < len(p) else p[0]
        change += graph[sub][left] + graph[sub][right]
    if best is None or best < change:
        print(p)
        best = change
print(best)
