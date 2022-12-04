import sys

c = 0
with open(sys.argv[1]) as fp:
    for l in fp.readlines():
        l = l.strip()
        nums = tuple(map(int, l.split("\t")))
        c += max(nums) - min(nums)

print(c)
