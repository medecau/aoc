import sys


fn = sys.argv[1]

with open(fn) as fp:
    data = fp.read().strip()
data = data + data
c = 0
for idx in range(int(len(data)/2)):
    if data[idx] == data[idx + int(len(data)/4)]:
        c+= int(data[idx])
print(c)
