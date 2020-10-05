from utils import get_input


address = get_input('1.txt')
current_floor = 0
basement_char = None

for n, c in enumerate(address):
    if c == '(':
        current_floor += 1
    elif c == ')':
        current_floor -= 1

    if current_floor < 0 and basement_char is None:
        basement_char = n + 1

print(current_floor, basement_char)
