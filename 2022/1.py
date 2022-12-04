import utils

rows = utils.get_lines(__file__)

callories = [0]

for row in rows:
    if not row:
        callories += [0]
        continue

    callories[-1] += int(row)

top = max(callories)
pos = callories.index(top)

print(pos + 1, top)

print(sum(sorted(callories)[-3:]))
