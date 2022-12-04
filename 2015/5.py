import re

import utils

strings = utils.get_lines(__file__)
p1 = re.compile(r".*(([a-z])\2)")
p2 = re.compile(r".*([aeiou].*[aeiou].*[aeiou])")
p3 = re.compile(r".*(ab|cd|pq|xy)")
p4 = re.compile(r".*(([a-z]{2}).*\2)")
p5 = re.compile(r".*(([a-z]).\2)")

"""
nice_strings = (s for s in strings if p1.match(s) is not None)
nice_strings = (s for s in nice_strings if p2.match(s) is not None)
nice_strings = (s for s in nice_strings if p3.match(s) is None)
"""
nice_strings = (s for s in strings if p4.match(s) is not None)
nice_strings = (s for s in nice_strings if p5.match(s) is not None)
print(len(list(nice_strings)))
