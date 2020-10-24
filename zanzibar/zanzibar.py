import sys

data = list(sys.stdin)[1:]

for row in data:
    l = list(map(int,row.split()))
    total = 0
    for i, num in enumerate(l[1:]):
        if l[i]*2 < num:
            total += (num - l[i]*2)
    print(total)
