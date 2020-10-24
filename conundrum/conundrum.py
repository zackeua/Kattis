import sys


l = list(sys.stdin)[0]

tot = 0
for i,c in enumerate(l[:-1]):
    if i%3 == 0:
        if c != "P":
            tot += 1
    if i%3 == 1:
        if c != "E":
            tot += 1
    if i%3 == 2:
        if c != "R":
            tot += 1

print(tot)
