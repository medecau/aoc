def desc(i):
    p = None
    for e in i:
        if p is None:
            p = e
            cntr = 1
        elif e != p:
            yield str(cntr)
            yield p
            cntr = 1
            p = e
        else:
            cntr += 1
    yield str(cntr)
    yield p


s = "3113322113"
for i in range(50):
    s = desc(s)

result = "".join(str(c) for c in s)
print(len(result))
