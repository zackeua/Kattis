import sys

data = list(map(int,list(sys.stdin)[1].split()))


print(data.index(min(data)))
