import sys

data = list(map(int,list(sys.stdin)[1].split()))

count = 0
average = 0
for d in data:
    if d != -1:
        average += d
        count += 1

print(average/count)
