import sys

data = list(sys.stdin)[0].split()

d = {}
vals = 'A23456789TJQK'
for v in vals:
    d[v] = 0
max = 0
for card in data:
    d[card[0]] += 1
    if d[card[0]] > max:
        max = d[card[0]]

print(max)
