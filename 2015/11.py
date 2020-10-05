import re

p1 = re.compile(r'[iol]')
p2 = re.compile(r'(([a-z])\2)')


def legal(s):
    p1m = p1.search(s)
    p2m = p2.findall(s)
    v = any(all(chr(ord(s[i + j]) + 1) == s[i + j + 1] for j in range(2)) for i in range(len(s) - 2))
    if p1m is None and \
       len(p2m) > 1 and \
       v:
        return True
    else:
        return False


def incr(s):
    done = False
    while not done or not legal(s):
        done = False
        pos = -1
        while not done:
            if s[pos] != 'z':
                done = True
                if pos == -1:
                    s = s[:pos] + chr(ord(s[pos]) + 1)
                else:
                    s = s[:pos] + chr(ord(s[pos]) + 1) + s[pos + 1:]
            else:
                if pos == -1:
                    s = s[:pos] + 'a'
                else:
                    s = s[:pos] + 'a' + s[pos + 1:]
                pos -= 1
    return s

next_pass = incr('cqjxjnds')
print(next_pass)
next_pass = incr(next_pass)
print(next_pass)


