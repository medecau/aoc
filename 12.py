import json

o = json.load(open('12.txt'))


while any(type(e) in (dict, list) for e in o):
    i = 0
    while i < len(o):
        if type(o[i]) in (dict, list):
            e = o.pop(i)
            if type(e) is dict and 'red' not in e.values():
                o.extend(e.values())
            else:
                o.extend(e)
        else:
            i += 1
o = [e for e in o if type(e) in (int, float)]
print sum(o)
