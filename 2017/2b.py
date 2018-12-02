import sys
from itertools import permutations

c=0
with open(sys.argv[1]) as fp:
    for l in fp.readlines():
        l = l.strip()
        nums = tuple(map(int, l.split('\t')))
        a,b = list(comb for comb in permutations(nums, 2) if comb[0]%comb[1]==0)[0]
        c += a/b


print(c)
