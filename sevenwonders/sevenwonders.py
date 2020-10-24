import sys


data = list(sys.stdin)[0]

l = [0,0,0]

for c in data:
    if c == 'T':
        l[0] += 1
    elif c == 'C':
        l[1] += 1
    elif c == 'G':
        l[2] += 1
print(l[0]**2 + l[1]**2 + l[2]**2 + 7*min(l))
