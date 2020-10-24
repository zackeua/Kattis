import sys

data = list(map(int,list(sys.stdin)[1].split()))

sum = 0
for value in data:
    if value < 0:
        sum += value
print(-sum)
