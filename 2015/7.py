import re
import sys
import time

import utils

instructions = """123 -> x
456 -> y
h AND g -> d
i OR f -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i""".split(
    "\n"
)
instructions = utils.get_lines(__file__)
instruction_pattern = re.compile(r"(.+) -> (\w+)$")
gate_pattern = re.compile(r"(?:^(\w+)\s)?([A-Z]+) (\w+)")

wires = dict()
for i in instructions:
    assignment_match = instruction_pattern.match(i)
    if assignment_match is None:
        raise RuntimeError
    else:
        value, wire = assignment_match.groups()
        wires[wire] = value

wires["b"] = "46065"


def resolve(wires):
    changed = False
    for w, v in wires.items():
        if type(v) is int:
            continue
        gate_match = gate_pattern.match(v)
        if gate_match is None and v.isalpha():
            wires[w] = wires[v]
        elif gate_match is not None:
            params = gate_match.groups()
            left, operator, right = params
            if left is not None and left in wires and left.isalpha():
                left = wires[left]
            if right.isalpha() and right in wires:
                right = wires[right]

            if operator == "NOT":
                if type(right) is int or right.isdigit():
                    wires[w] = 0xFFFF ^ int(right)
                    changed = True

            elif operator in ("AND", "OR"):
                if (type(left) is int or left.isdigit()) and (
                    type(right) is int or right.isdigit()
                ):
                    if params[1] == "AND":
                        wires[w] = int(left) & int(right)
                        changed = True
                    else:
                        wires[w] = int(left) | int(right)
                        changed = True

            elif operator in ("LSHIFT", "RSHIFT"):
                if type(left) is int or left.isdigit():
                    if params[1] == "LSHIFT":
                        wires[w] = int(left) << int(right)
                        changed = True
                    else:
                        wires[w] = int(left) >> int(right)
                        changed = True
    return changed


def show(wires):
    for w, v in wires.items():
        print("%s: %s" % (w, v))


show(wires)
c = 0
while resolve(wires):
    c += 1
    print(c)
    # show(wires)
print(wires["a"])
