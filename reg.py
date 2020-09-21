import re
s = '345 manan ans, 45 234 2222 mananarora200@gmail.com as'
pattern = re.compile(r'([a-zA-Z0-9]+@[a-z]+.com)')
for i in pattern.finditer(s):
    print(i.group(1))