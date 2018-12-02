import sys


fn = sys.argv[1]

with open(fn) as fp:
    data = fp.read().strip()
data += data[0]
c = 0
for idx in range(len(data)-1):
    if data[idx] == data[idx+1]:
        c+= int(data[idx])
print(c)
