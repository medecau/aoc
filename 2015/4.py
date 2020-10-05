import hashlib


def hex_hash(s):
    h = hashlib.md5()
    h.update(s.encode())
    return h.hexdigest()

zeros = '0' * 6
key = 'ckczppom'

num = 0
while True:
    num += 1
    s = key + str(num)
    r = hex_hash(s)
    if r.startswith(zeros):
        break
print(num, s)
