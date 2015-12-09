from utils import get_input
import re


lines = r'''""
"abc"
"aaa\"aaa"
"\x27"'''.splitlines()

lines = get_input('8.txt').split('\n')
for l in lines:
    print
    print l
    print l.decode('string-escape')
    print re.escape(l)
string_code = sum(len(l) for l in lines)
memory_characters = sum(len(l[1:-1].decode('string_escape')) for l in lines)
encoded_strings = sum(len(re.escape(l)) + 2 for l in lines)
print string_code, memory_characters, encoded_strings
print string_code - memory_characters
print encoded_strings - string_code
