import re
from re import match

p = re.compile('sb')
print(p.match("tempo"))
print(p.match("rahul"))
print(p.match("bhushan"))
print(p.match("abcd"))
print(p.match("abbbbbhsdai"))
print(p.match("aaaaabbbbbhvrb"))
