import re

exp = ":\)|;\)|:-\)|;-\)"
s = input()

l = re.finditer(exp, s)

for item in l:
    print(item.start(0))
