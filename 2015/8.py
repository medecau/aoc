import re

import utils

lines = r'''""
"abc"
"aaa\"aaa"
"\x27"'''.splitlines()

lines = utils.get_lines(__file__)
for l in lines:
    print()
    print(l)
    print(l.encode().decode("unicode-escape"))
    print(re.escape(l))
string_code = sum(len(l) for l in lines)
memory_characters = sum(len(l[1:-1].encode().decode("unicode_escape")) for l in lines)
encoded_strings = sum(len(re.escape(l)) + 2 for l in lines)
print(string_code, memory_characters, encoded_strings)
print(string_code - memory_characters)
print(encoded_strings - string_code)
