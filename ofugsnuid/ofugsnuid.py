import sys


data = list(sys.stdin)

data = data[::-1]

data = data[:-1]

for elem in data:
    print(elem)
